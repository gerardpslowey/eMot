import pandas as pd
import re, textMod
from sklearn.linear_model import LogisticRegression

# TODO look into tfidf
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# TODO look into implementing a pipeline
from sklearn.pipeline import Pipeline

def custom_sentiment(sentiment):
    if sentiment == "neg":
        return 0
    else:
        return 1


def main():
    # read the dataset into a data frame
    df = pd.read_csv("datasets/train.csv")

    # remove neutrals for the moment
    df = df[df.Sentiment != "other"]    
    df['CustomSentiment'] = df.apply(lambda x: custom_sentiment(x['Sentiment']), axis=1)
    df['Tweet'] = df['Tweet'].apply(textMod.pre_process)
    df['Tweet'] = df['Tweet'].apply(textMod.tokenise)

    # convert the text to a matrix of word counts
    vectorizer = CountVectorizer(analyzer = 'word', stop_words='english')
    bag_of_words = vectorizer.fit_transform(df.Tweet)

    sentimentLabels = df.CustomSentiment

    X_train, X_test, y_train, y_test = train_test_split(
        bag_of_words, 
        sentimentLabels, 
        train_size=0.8)

    # for c in [0.01, 0.05, 0.25, 0.5, 1]:
    #     lr = LogisticRegression(C=0.05)
    #     lr.fit(X_train, y_train)
    #     print('Accuracy for C=%s: %s'
    #         % (c, accuracy_score(y_test, lr.predict(X_test))))

    final_model = LogisticRegression()

    # train the model to the dataset
    final_model.fit(X_train, y_train)
    print('Final Model Accuracy: %s' % accuracy_score(y_test, final_model.predict(X_test)))    

    feature_to_coef = {
        word: coef for word, coef in zip(
        vectorizer.get_feature_names(), final_model.coef_[0])
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