import pandas as pd
import re, pickle, textMod, numpy as np
import cProfile, io, pstats

from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split, GridSearchCV

# TODO look into implementing a pipeline
from sklearn.pipeline import Pipeline

def calculateCValue(x_train_fit, y_train):
    param_grid = {'C': [0.001, 0.01, 0.05, 0.25, 0.5, 1, 10]}
    grid = GridSearchCV(LogisticRegression(), param_grid, cv=5)
    grid.fit(x_train_fit, y_train)
    print("Best cross-validation score: {:.2f}".format(grid.best_score_))
    print("Best parameters: {}".format(grid.best_params_))
    return grid.best_params_

def negAndPos(cv, model):
    feature_to_coef = {
        word: coef for word, coef in zip(cv.get_feature_names(), model.coef_[0])}

    print('Positive Words')
    bp =[]
    for best_positive in sorted(feature_to_coef.items(), key=lambda x: x[1], reverse=True) [:25]: 
            print(best_positive)
            bp.append(best_positive[0])

    print('Negative Words')
    bn=[]
    for best_negative in sorted(feature_to_coef.items(), key=lambda x: x[1])[:10]:
            print(best_negative)
            bn.append(best_negative[0])

    textMod.wordcloud_draw(bp)
    #wp.wordcloud_draw(bn)

def saveFiles(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)

def customSentiment(sentiment):
    return 0 if sentiment == "neg" else 1

def main():
    # read the dataset into a data frame
    trainSet = pd.read_csv("../datasets/train.csv")

    # remove neutrals for the moment
    trainSet = trainSet[trainSet.Sentiment != "other"]    
    trainSet['CustomSentiment'] = trainSet.apply(lambda x: customSentiment(x['Sentiment']), axis=1)
    trainSet['Tweet'] = trainSet['Tweet'].apply(textMod.preProcess)

    X = trainSet.Tweet
    y = trainSet.CustomSentiment

    x_train, x_test, y_train, y_test = train_test_split(X, y,
                                                        test_size=0.2, 
                                                        shuffle=True)
    cv = CountVectorizer()
    x_train_fit = cv.fit_transform(x_train)
    x_test_transform = cv.transform(x_test)

    #calculateCValue(x_train_fit, y_train)
    model = LogisticRegression()
    model.fit(x_train_fit, y_train)         # train the model to the dataset

    y_pred_class = model.predict(x_test_transform)
    aScore = accuracy_score(y_test, y_pred_class)
    print("Final Model Accuracy: {:.2f}".format(aScore))

    negAndPos(cv, model)                    # print the most negative and positive words

    model_filename = "LR_Model.pkl" 
    saveFiles(model, model_filename)      # save the model

    cv_filename = "CV_File.pkl"
    saveFiles(cv, cv_filename)

if __name__ == '__main__':
    main()
    # pr = cProfile.Profile()
    # pr.enable()

    # my_result = main()

    # pr.disable()
    # s = io.StringIO()
    # ps = pstats.Stats(pr, stream=s).sort_stats('tottime')
    # ps.print_stats()

    # with open('scikit_cprofile.txt', 'w+') as f:
    #     f.write(s.getvalue())