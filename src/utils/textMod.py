import spacy, re

from spellchecker import SpellChecker
spell = SpellChecker(distance=1)

from spacy.tokenizer import _get_regex_pattern

# load spacy data file
nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])

# get default pattern for tokens that don't get split
re_token_match = _get_regex_pattern(nlp.Defaults.token_match)
re_token_match = fr'({re_token_match}|#\w+|\w+-\w+)'

# overwrite token_match function of the tokenizer
nlp.tokenizer.token_match = re.compile(re_token_match).match


# Used for training models on datasets
def preprocessAndTokenise(data):
    data = removehtmlMarkup(data)
    data = removeURLs(data)
    data = removeHashandSymbols(data)
    data = removeAscii(data)
    data = removeEmojis(data)
    data = data.strip()

    mytokens = nlp(data)

    stem_data = [
        word.lemma_.strip() for word in mytokens
        if not word.is_punct and not word.is_stop and not word.is_space and not word.is_digit
    ]

    return stem_data


# cleaned scraped text
def preProcess(data):
    data = removehtmlMarkup(data)
    data = removeURLs(data)
    data = removeHashandSymbols(data)
    data = removeAscii(data)
    data = data.strip()
    # tokenise
    mytokens = nlp(data)

    stem_data = [
        word.lemma_.strip() for word in mytokens
        if word.lemma_ != '-PRON-'
        and not word.is_punct and not word.is_stop and not word.is_space and not word.is_digit  # noqa: W503
    ]
    return " ".join(stem_data)


# remove html markup tags
def removehtmlMarkup(sentence):
    return re.sub("(<.*?>)", "", sentence)


# remove urls
def removeURLs(sentence):
    return re.sub(r'https?://\S+|www\.\S+', "", sentence)


# remove hashtags and @ symbols
def removeHashandSymbols(sentence):
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
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "]+",
        flags=re.UNICODE
    )
    return regrex_pattern.sub(r"", text)
