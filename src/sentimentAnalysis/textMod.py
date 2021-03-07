import spacy, re, string
nlp = spacy.load('en_core_web_sm')

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
            and not word.is_punct
            and '@' not in word.text):
            
            cleaned.append(word.lemma_.strip())

    # return preprocessed list of tokens
    return " ".join(cleaned)