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
    data = data.strip()

    mytokens = nlp(data)

    stem_data = [
        word.lemma_.strip() for word in mytokens
        if not word.is_punct and not word.is_stop and not word.is_space
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
        if word.lemma_ != '-PRON-' and not word.is_punct and not word.is_stop and not word.is_space
    ]

    return " ".join(stem_data)


# remove html markup
def removehtmlMarkup(sentence):
    return re.sub("(<.*?>)", "", sentence)


# remove urls
def removeURLs(sentence):
    return re.sub(r'https?://\S+|www\.\S+', '', sentence)


# remove hashtags and @ symbols
def removeHashandSymbols(sentence):
    # hash symbols
    data = re.sub(r"(#[\d\w\.]+)", '', sentence)
    # @ symbols
    return re.sub(r"(@[\d\w\.]+)", '', data)


# remove punctuation and non-ascii digits
def removeAscii(sentence):
    return re.sub("(\\W|\\d)", " ", sentence)


# Keeping this works great
def spellCheck(sentence):
    words = spell.split_words(sentence)
    return " ".join([spell.correction(word) for word in words])
