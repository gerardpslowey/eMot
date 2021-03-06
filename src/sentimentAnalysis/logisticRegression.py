import pandas as pd
import re, textMod, pickle
from sklearn.linear_model import LogisticRegression

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV

# TODO look into implementing a pipeline
from sklearn.pipeline import Pipeline

def customSentiment(sentiment):
    if sentiment == "neg":
        return 0
    else:
        return 1

def calculateCValue(trainFit, y_train):
    param_grid = {'C': [0.001, 0.01, 0.05, 0.25, 0.5, 1, 10]}
    grid = GridSearchCV(LogisticRegression(), param_grid, cv=5)
    grid.fit(trainFit, y_train)
    print("Best cross-validation score: {:.2f}".format(grid.best_score_))
    print("Best parameters: {}".format(grid.best_params_))
    return grid.best_params_

def negAndPos(cv, model):
    feature_to_coef = {
    word: 
        coef for word, coef in zip(cv.get_feature_names(), model.coef_[0])
    }

    print('Positive Words')
    for best_positive in sorted(
        feature_to_coef.items(), 
        key=lambda x: x[1], reverse=True) [:10]: 
        print(best_positive)

    print('Negative Words')
    for best_negative in sorted(
        feature_to_coef.items(),
        key=lambda x: x[1])[:10]:
        print(best_negative)

def saveFiles(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)


def checkAccuracy(testTransform, y_test, model):
    y_pred_class = model.predict(testTransform)
    aScore = accuracy_score(y_test, y_pred_class)

    print("Final Model Accuracy: {:.2f}".format(aScore)) 

def main():
    # read the dataset into a data frame
    trainSet = pd.read_csv("datasets/train.csv")

    # remove neutrals for the moment
    trainSet = trainSet[trainSet.Sentiment != "other"]    
    trainSet['CustomSentiment'] = trainSet.apply(lambda x: customSentiment(x['Sentiment']), axis=1)
    trainSet['Tweet'] = trainSet['Tweet'].apply(textMod.pre_process)
    # trainSet['Tweet'] = trainSet['Tweet'].apply(textMod.tokenise)

    X = trainSet.Tweet
    y = trainSet.CustomSentiment
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8)

    cv = CountVectorizer()
    trainFit = cv.fit_transform(X_train)
    testTransform = cv.transform(X_test)

    # cValue = calculateCValue(trainFit, y_train)
    model = LogisticRegression()
    # train the model to the dataset
    model.fit(trainFit, y_train)

    checkAccuracy(testTransform, y_test, model)

    # print the most negative and positive words
    negAndPos(cv, model)

    model_filename = "LR_Model.pkl"
    cv_filename = "CV_File.pkl"

    # save the model
    saveFiles(model, model_filename)
    saveFiles(cv, cv_filename)

if __name__ == '__main__':
    main()