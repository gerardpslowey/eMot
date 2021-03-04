import spacy, re, string, nltk
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.lang.en import English
from sklearn.base import TransformerMixin
from nltk.corpus import stopwords

punc_set = set(string.punctuation)
# nltk.download('stopwords')

stop_set = set(stopwords.words('english'))

nlp = spacy.load('en_core_web_sm')

def tokenise(sentence):
    # Creating our token object, which is used to create documents with linguistic annotations.
    mytokens = nlp(sentence)

    # Lemmatizing each token and converting each token into lowercase
    #  if word.lemma_ != "-PRON-" else word.lower_
    mytokens = [word.lemma_.lower().strip() for word in mytokens]
 
    # Removing stop words
    mytokens = [word for word in mytokens if word not in stop_set and word not in punc_set]

    # return preprocessed list of tokens
    return " ".join(mytokens)

def pre_process(text):
    # lowercase
    text = text.strip().lower()
    # tags
    text = re.sub('&lt;/?.*?&gt;', '&lt;&gt;', text)
    # special characters and digits
    text=re.sub('(\\d|\\W)+', ' ',text)

    text=re.sub('<[^>]*>','',text)
    # filter emojis
    emojis=re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)',text)

    text=re.sub('[\W]+',' ',text.lower()) + ' '.join(emojis).replace('-','')
    
    return text