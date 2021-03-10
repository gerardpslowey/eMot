import pandas as pd
import re, pickle, textMod, numpy as np
import cProfile, io, pstats
from tqdm import tqdm
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split, GridSearchCV

# TODO look into implementing a pipeline
from sklearn.pipeline import Pipeline

sentiment_dict = {"neutral": 0, "worry":1, "happiness":2, "sadness":3, "love":4, "surprise":5, "fun":6, "relief":7, "hate":8, "empty":9, "enthusiasm":10, "boredom":11, "anger":12}

def calculateCValue(x_train_fit, y_train):
    param_grid = {'C': [0.01, 0.05, 0.25, 0.5, 1, 10]}
    grid = GridSearchCV(LogisticRegression(), param_grid, cv=5)
    grid.fit(x_train_fit, y_train)
    # print("Best cross-validation score: {:.2f}".format(grid.best_score_))
    print("Best parameters: {}".format(grid.best_params_))
    return grid.best_params_

def saveFiles(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)

def customSentiment(sentiment):
    return sentiment_dict[sentiment]

def main():
    # read the dataset into a data frame
    print("Reading Training Data")
    trainSet = pd.read_csv("../datasets/text_emotion.csv")
    print("Finished Reading")

    print("\nCleaning Data Set")
    trainSet['CustomSentiment'] = trainSet.apply(lambda x: customSentiment(x['sentiment']), axis=1)
    trainSet['content'] = trainSet['content'].apply(textMod.preProcess)
    print("Finished Cleaning")

    X = trainSet.content
    y = trainSet.CustomSentiment

    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=True)

    cv = CountVectorizer()
    x_train_fit = cv.fit_transform(x_train)
    x_test_transform = cv.transform(x_test)

    # c = calculateCValue(x_train_fit, y_train))

    model = LogisticRegression(multi_class='multinomial', solver='lbfgs')
    model.fit(x_train_fit, y_train)         

    y_pred_class = model.predict(x_test_transform)
    aScore = accuracy_score(y_test, y_pred_class)
    print("Final Model Accuracy: {:.2f}".format(aScore))


    model_filename = "../models/LRModelEmotion.pkl" 
    saveFiles(model, model_filename)      
    
    cv_filename = "../models/CVFileEmotions.pkl"
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