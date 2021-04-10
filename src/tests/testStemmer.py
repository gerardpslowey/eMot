import spacy, stanza, nltk, time  # noqa

from nltk import word_tokenize
from nltk.stem import PorterStemmer


def stanzaLemma(sentences):
    nlp = stanza.Pipeline(lang='en', processors='tokenize, pos, lemma')

    start = time.time()
    for sentence in sentences:
        doc = nlp(sentence)
        [word.lemma.strip() for sent in doc.sentences for word in sent.words]
        # print(stem_data)
        # return stem_data
    end = time.time()
    print("Stanza Time: {} seconds".format(end - start))


def spacyLemma(sentences):
    nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])

    start = time.time()
    for sentence in sentences:
        mytokens = nlp(sentence)
        [word.lemma_.strip() for word in mytokens]
        # return stem_data
    end = time.time()
    print("Spacy Time: {} seconds".format(end - start))


def nltkPorter(sentences):
    porter = PorterStemmer()

    start = time.time()
    for sentence in sentences:
        data = word_tokenize(sentence)
        [porter.stem(word).strip() for word in data]
        # print(stem_data)
        # return stem_data
    end = time.time()
    print("NLTK Time: {} seconds".format(end - start))


if __name__ == '__main__':
    sentences = [
        "Wondering why I'm awake at 7am,writing a new song,plotting my evil secret plots muahahaha...oh damn it,not secret anymore",  # noqa
        "No Topic Maps talks at the Balisage Markup Conference 2009   Program online at http://tr.im/mL6Z (via @bobdc) #topicmaps",  # noqa
        "I ate Something I don't know what it is... Why do I keep Telling things about food",
        "so tired and i think i'm definitely going to get an ear infection.  going to bed &quot;early&quot; for once.",
        "On my way home n having 2 deal w underage girls drinking gin on da bus while talking bout keggers......damn i feel old"  # noqa
    ]

    stanzaLemma(sentences)
    spacyLemma(sentences)
    nltkPorter(sentences)
