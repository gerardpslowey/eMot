from spellchecker import SpellChecker
spell = SpellChecker(distance=1)

import spacy, re, string
from spacy.tokenizer import _get_regex_pattern
nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
nlp.add_pipe('sentencizer')

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# get default pattern for tokens that don't get split
re_token_match = _get_regex_pattern(nlp.Defaults.token_match)
re_token_match = f"({re_token_match}|#\w+|\w+-\w+)"

# overwrite token_match function of the tokenizer
nlp.tokenizer.token_match = re.compile(re_token_match).match

def preProcess(sentence):
    mytokens = nlp(sentence.lower())

    cleaned = []
    for word in mytokens:
        if (word.lemma_ != '-PRON-'
            and '@' not in word.text and '#' not in word.text 
            and not word.is_punct and not word.is_stop):            
            
            cleaned.append(word.lemma_.strip())

    return " ".join(cleaned)

def removeURLs(sentence):
    url = re.compile(r'https?://\S+|www\.\S+')
    return url.sub(r'', sentence)

def removeRepetitions(sentence):
    pattern = re.compile(r"(.)\1{2,}")          
    return pattern.sub(r"\1\1", sentence)

def spellCheck(sentence):
    words = spell.split_words(sentence)
    return " ".join([spell.correction(word) for word in words])

def wordcloud_draw(data, color = 'white'):
    words = ' '.join(data)
    wordcloud = WordCloud(  background_color=color,
                            width=2500, height=2000).generate(words)
    plt.figure(1,figsize=(10, 7))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()