from spellchecker import SpellChecker
spell = SpellChecker()

import spacy, re, string
nlp = spacy.load('en_core_web_sm')

from wordcloud import WordCloud
import matplotlib.pyplot as plt

def spellChecker(sentence):
    corrected_text = []
    misspelled_words = spell.unknown(sentence.split())
    for word in sentence.split():
        if word in misspelled_words:
            corrected_text.append(spell.correction(word))
        else:
            corrected_text.append(word)
    return " ".join(corrected_text)

def preProcess(sentence):
    #remove urls
    url = re.compile(r'https?://\S+|www\.\S+')
    sentence = url.sub(r'',sentence)

    #remove html tags
    html = re.compile(r'<.*?>')
    sentence = html.sub(r'',sentence)

    # Creating our token object, which is used to create documents with linguistic annotations.
    mytokens = nlp(sentence.lower())

    # Removing stop words
    cleaned = []
    for word in mytokens:

        if (word.lemma_ != '-PRON-' 
            and not word.is_stop
            and '@' not in word.text
            and '#' not in word.text 
            and not word.is_punct):
            
            cleaned.append(word.lemma_.strip())

    # return preprocessed list of tokens
    return " ".join(cleaned)


def wordcloud_draw(data, color = 'white'):
    words = ' '.join(data)
    wordcloud = WordCloud(background_color=color,
                            width=2500,
                            height=2000).generate(words)
    plt.figure(1,figsize=(10, 7))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()