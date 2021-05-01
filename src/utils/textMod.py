import re
import string

import spacy
from spacy.tokenizer import _get_regex_pattern
from spellchecker import SpellChecker

spell = SpellChecker(distance=1)


# load spacy data file
nlp = spacy.load("en_core_web_sm", disable=["parser", "ner"])

# get default pattern for tokens that don't get split
re_token_match = _get_regex_pattern(nlp.Defaults.token_match)
re_token_match = fr"({re_token_match}|#\w+|\w+-\w+)"

# overwrite token_match function of the tokenizer
nlp.tokenizer.token_match = re.compile(re_token_match).match


# Used for training models on datasets
def preprocessAndTokenise(data):
    data = removehtmlMarkup(data)
    data = removeURLs(data)
    data = removeHashAndSymbols(data)
    data = removeAscii(data)
    data = removeEmojis(data)
    data = data.strip()

    mytokens = nlp(data)

    stem_data = [
        word.lemma_.strip()
        for word in mytokens
        if not word.is_punct
        and not word.is_stop
        and not word.is_space
        and not word.is_digit
    ]

    return stem_data


# cleaned scraped text
def preProcess(data):
    data = removehtmlMarkup(data)
    data = removeURLs(data)
    data = removeHashAndSymbols(data)
    data = data.strip()

    # tokenise, remove punctuation and spaces
    mytokens = nlp(data)
    filtered = [
        word.text.strip()
        for word in mytokens
        if not word.is_punct
        and not word.is_space
    ]
    return " ".join(filtered)


def clean(data):
    data = data.split("|")

    filtered = []

    for sentence in data:
        mytokens = nlp(sentence)
        stem_data = [
            word.lemma_.strip()
            for word in mytokens
            if word.lemma_ != "-PRON-"
            and not word.is_punct
            and not word.is_stop
            and not word.is_space
            and not word.is_digit  # noqa: W503
        ]
        filtered.append(" ".join(stem_data))

    return "|".join(filtered)


# remove html markup tags
def removehtmlMarkup(sentence):
    return re.sub("(<.*?>)", "", sentence)


# remove urls
def removeURLs(sentence):
    return re.sub(r"https?://\S+|www\.\S+", "", sentence)


# remove hashtags and @ symbols
def removeHashAndSymbols(sentence):
    # hash symbols
    data = re.sub(r"(#[\d\w\.]+)", "", sentence)
    # @ symbols
    return re.sub(r"(@[\d\w\.]+)", "", data)


# remove non-ascii digits
def removeAscii(sentence):
    return re.sub("(\\d)", "", sentence)


# Keeping this works great
def spellCheck(sentence):
    words = spell.split_words(sentence)
    return " ".join([spell.correction(word) for word in words])


def removeEmojis(text):
    regrex_pattern = re.compile(
        pattern="["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "]+",
        flags=re.UNICODE,
    )
    return regrex_pattern.sub(r"", text)
