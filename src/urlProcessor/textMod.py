import spacy, re, string, os, pickle, matplotlib.pyplot as plt

from spacy.tokenizer import _get_regex_pattern
nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
nlp.add_pipe('sentencizer')

from wordcloud import WordCloud
from pathlib import Path

# text preprocessing
from nltk import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import re

from spellchecker import SpellChecker
spell = SpellChecker(distance=1)

# get default pattern for tokens that don't get split
re_token_match = _get_regex_pattern(nlp.Defaults.token_match)
re_token_match = fr'({re_token_match}|#\w+|\w+-\w+)'

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


def preprocess_and_tokenize(data):    

    #remove html markup
    data = re.sub("(<.*?>)", "", data)

    #remove urls
    data = re.sub(r'http\S+', '', data)
    
    #remove hashtags and @names
    data = re.sub(r"(#[\d\w\.]+)", '', data)
    data = re.sub(r"(@[\d\w\.]+)", '', data)

    #remove punctuation and non-ascii digits
    data = re.sub("(\\W|\\d)", " ", data)
    
    #remove whitespace
    data = data.strip()
    
    # tokenization with nltk
    data = word_tokenize(data)
    
    # stemming with nltk
    porter = PorterStemmer()
    stem_data = [porter.stem(word) for word in data]
        
    return stem_data

def wordcloud_draw(data, color = 'white'):
    words = ' '.join(data)
    wordcloud = WordCloud(
        background_color=color, 
        width=2500, height=2000).generate(words)

    plt.figure(1,figsize=(10, 7))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()


def saveFiles(data, filename):
    directory = "../models"
    if not os.path.exists(directory):
        Path(directory).mkdir(parents=True, exist_ok=True)

    model_location = os.path.join(directory, filename)
    with open(model_location, 'wb') as file:
        pickle.dump(data, file)
    print("Model and Data Saved")