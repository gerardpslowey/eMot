import pandas as pd, re, numpy as np, pickle

from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from nltk.corpus import wordnet
from nltk.corpus import stopwords
stop = stopwords.words('english')
import random

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.absolute())) 
from urlProcessor.textMod import preProcess, removeURLs, removeRepetitions, spellCheck

from tqdm import tqdm
tqdm.pandas()

def main():
    # read the dataset into a data frame
    df = pd.read_csv("../datasets/text_emotion.csv")
    df.set_index('tweet_id', inplace=True)

    df = df.drop(df[df.sentiment == 'boredom'].index)
    df = df.drop(df[df.sentiment == 'surprise'].index)
    df = df.drop(df[df.sentiment == 'enthusiasm'].index)
    df = df.drop(df[df.sentiment == 'empty'].index)
    df = df.drop(df[df.sentiment == 'fun'].index)
    df = df.drop(df[df.sentiment == 'relief'].index)
    df = df.drop(df[df.sentiment == 'love'].index)
    df = df.drop(df[df.sentiment == 'neutral'].index)

    df['sentiment'].replace(to_replace='hate', value='anger', inplace=True)
    # replace 'worry' for 'fear'
    df['sentiment'].replace(to_replace='worry', value='fear', inplace=True)

    anger = df.loc[df['sentiment'] == 'anger']
    new_anger_comments = []
    for content in anger['content']:
        new_anger_comments.append(synonym_replacement(content, 4))
        new_anger_comments.append(random_insertion(content, 4))
    new_anger = pd.DataFrame()
    new_anger['content'] = new_anger_comments
    new_anger['sentiment'] = 'anger'
    anger = anger.append(new_anger)
    df = df.append(new_anger)

    #print(df.groupby('sentiment')['sentiment'].count().sort_values(ascending=False))


    df['content'] = df['content'].progress_apply(preProcess)
    df['content'] = df['content'].progress_apply(removeURLs)
    df['content'] = df['content'].progress_apply(removeRepetitions)
    df['content'] = df['content'].progress_apply(spellCheck)

    #Encoding output labels
    lbl_enc = LabelEncoder()
    y = lbl_enc.fit_transform(df.sentiment.values)
    X = df.content.values

    X_train, X_val, y_train, y_val = train_test_split(           
            X, y, random_state=42, test_size=0.2, shuffle=True)

    # tfidf = TfidfVectorizer(max_features=1000,ngram_range=(1,3))
    # X_train_tfidf = tfidf.fit_transform(X_train)
    # X_val_tfidf = tfidf.fit_transform(X_val)

    cv = CountVectorizer()          #analyzer='word'
    cv.fit(df['content'])
    X_train_count =  cv.transform(X_train)
    X_val_count =  cv.transform(X_val)

    #alpha = loss checker
    lsvm = SGDClassifier(alpha=0.001, loss='modified_huber', penalty = 'l2', random_state=5, max_iter=15, tol=None)
    lsvm.fit(X_train_count, y_train)
    y_pred = lsvm.predict(X_val_count)
    print('lsvm using count vectors accuracy %s' % accuracy_score(y_pred, y_val))

    # fear         8459
    # happiness    5209
    # sadness      5165
    # anger        1433
    feature_to_coef = {
        word: coef for word, coef in zip(cv.get_feature_names(), lsvm.coef_[0])}

    print('Anger Words')
    for best_positive in sorted(feature_to_coef.items(), key=lambda x: x[1], reverse=True) [:20]: 
        print(best_positive)

    print('Fear Words')
    for best_positive in sorted(feature_to_coef.items(), key=lambda x: x[1]) [:20]: 
        print(best_positive)

    model_filename = "../models/sgd_Model.pkl" 
    saveFiles(lsvm, model_filename)      # save the model

    cv_filename = "../models/sgd_CV_File.pkl"
    saveFiles(cv, cv_filename)

def saveFiles(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)

def get_synonyms(word):
    #Get synonyms of a word
    synonyms = set()
    
    for syn in wordnet.synsets(word): 
        for l in syn.lemmas(): 
            synonym = l.name().replace("_", " ").replace("-", " ").lower()
            synonym = "".join([char for char in synonym if char in ' qwertyuiopasdfghjklzxcvbnm'])
            synonyms.add(synonym) 
    
    if word in synonyms:
        synonyms.remove(word)
    
    return list(synonyms)

def synonym_replacement(words, n):
    
    words = words.split()
    new_words = words.copy()
    random_word_list = list(set([word for word in words if word not in stop]))
    random.shuffle(random_word_list)
    num_replaced = 0
    
    for random_word in random_word_list:
        synonyms = get_synonyms(random_word)
        
        if len(synonyms) >= 1:
            synonym = random.choice(list(synonyms))
            new_words = [synonym if word == random_word else word for word in new_words]
            num_replaced += 1
        
        if num_replaced >= n: #only replace up to n words
            break
    return ' '.join(new_words)

# Random Insertion
def random_insertion(words, n):
    
    words = words.split()
    new_words = words.copy()
    
    for _ in range(n):
        add_word(new_words)
        
    sentence = ' '.join(new_words)
    return sentence

def add_word(new_words):
    synonyms = []
    counter = 0
    
    while len(synonyms) < 1:
        random_word = new_words[random.randint(0, len(new_words)-1)]
        synonyms = get_synonyms(random_word)
        counter += 1
        if counter >= 10:
            return
        
    random_synonym = synonyms[0]
    random_idx = random.randint(0, len(new_words)-1)
    new_words.insert(random_idx, random_synonym)

if __name__ == '__main__':
    main()