import pandas as pd
import re, pickle, numpy as np, sys
import cProfile, io, pstats

from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split, GridSearchCV

from sklearn.pipeline import Pipeline

from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.absolute())) 
from urlProcessor.textMod import saveFiles, preprocess_and_tokenize

def calculateCValue(x_train_fit, y_train):
    param_grid = {'C': [0.01, 0.05, 0.25, 0.5, 1, 10]}
    grid = GridSearchCV(LogisticRegression(), param_grid, cv=5)
    grid.fit(x_train_fit, y_train)
    # print("Best cross-validation score: {:.2f}".format(grid.best_score_))
    print("Best parameters: {}".format(grid.best_params_))
    return grid.best_params_

def main():
    # read the dataset into a data frame
    print("Reading Training Data")
    df_train = pd.read_csv('../datasets/data_train.csv')
    df_test = pd.read_csv('../datasets/data_test.csv')

    X_train = df_train.Text
    x_test = df_test.Text

    y_train = df_train.Emotion
    y_test = df_test.Emotion

    data = pd.concat([df_train, df_test])
    print("Finished Reading")

    # print(trainSet.Sentiment.value_counts())
    
    vect = CountVectorizer()
    X_train_vect = vect.fit_transform(X_train)
    X_test_vect = vect.transform(x_test)

    model = LogisticRegression(C=0.1, multi_class='auto', solver='lbfgs', max_iter=200, penalty='l2')
    model.fit(X_train_vect, y_train)

    y_pred = model.predict(X_test_vect)
    print("Accuracy: {:.2f}%".format(accuracy_score(y_test, y_pred) * 100))
    print("F1 Score: {:.2f}".format(f1_score(y_test, y_pred, average='micro') * 100))

    model_filename = 'lr.pkl'
    cv_filename = 'lr_cv.pkl'
    saveFiles(model, model_filename)
    saveFiles(vect, cv_filename)

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