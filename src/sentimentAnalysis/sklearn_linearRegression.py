import pandas as pd
import sys, textMod, re
from pathlib import Path
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

def custom_sentiment(sentiment):
    if sentiment == "neg":
        return -1
    elif sentiment == "pos":
        return 1
    else:
        return 0

def pre_process(text):
    # lowercase
    text = text.lower()
    # tags
    text = re.sub('&lt;/?.*?&gt;', '&lt;&gt;', text)
    # special characters and digits
    text=re.sub('(\\d|\\W)+', ' ',text)
    
    return text

def main():
    # read the dataset into a data frame
    df = pd.read_csv("datasets/train.csv")

    # select all the rows from the 1st and 5th column
    # tweet_text = df['Tweet'].values
    # sentiment_label = df['Sentiment'].values

    df['CustomSentiment'] = df.apply(lambda x: custom_sentiment(x['Sentiment']), axis=1)
    df['Tweet'] = df['Tweet'].apply(lambda x: pre_process(x))

    cv = CountVectorizer(stop_words='english')
    cv.fit(df['Tweet'])

    X = cv.transform(df['Tweet'])
    y = df['CustomSentiment']

    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.75)

    # for c in [0.01, 0.05, 0.25, 0.5, 1]:
        
    #     lr = LogisticRegression(C=c)
    #     lr.fit(X_train, y_train)
    #     print('Accuracy for C=%s: %s'
    #         % (c, accuracy_score(y_test, lr.predict(X_test))))

    final_model = LogisticRegression(C=1)
    final_model.fit(X, y)
    print('Final Model Accuracy: %s' %accuracy_score(y_test, final_model.predict(X_test)))


    feature_to_coef = {
        word: coef for word, coef in zip(
        cv.get_feature_names(), final_model.coef_[0])
    }

    print('Positive Words')
    for best_positive in sorted(
        feature_to_coef.items(), 
        key=lambda x: x[1], reverse=True) [:10]: print(best_positive)

    print('Negative Words')
    for best_negative in sorted(
        feature_to_coef.items(),
        key=lambda x: x[1])[:10]:
        print(best_negative)

if __name__ == '__main__':
    main()