import re, nltk
from nltk import word_tokenize
from nltk.stem import PorterStemmer

def preprocess_and_tokenize(data):    
    # remove html markup
    data = re.sub("(<.*?>)", "", data)

    # remove urls
    data = re.sub(r'https?://\S+|www\.\S+', '', data)
    
    # remove hashtags and @ symbols
    data = re.sub(r"(#[\d\w\.]+)", '', data)
    data = re.sub(r"(@[\d\w\.]+)", '', data)

    # remove punctuation and non-ascii digits
    data = re.sub("(\\W|\\d)", " ", data)
    
    # remove whitespace
    data = data.strip()
    
    # tokenization with nltk
    data = word_tokenize(data)
    
    # stemming with nltk
    porter = PorterStemmer()
    stem_data = [porter.stem(word) for word in data]
        
    return stem_data
