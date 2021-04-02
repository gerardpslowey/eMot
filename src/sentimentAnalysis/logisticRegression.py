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
    grid = GridSearchCV(LogisticRegression(), param_grid, vect=5)
    grid.fit(x_train_fit, y_train)
    # print("Best cross-validation score: {:.2f}".format(grid.best_score_))
    print("Best parameters: {}".format(grid.best_params_))
    return grid.best_params_

def main():
    df_anger = pd.read_csv('../datasets/anger.csv')
    df_fear = pd.read_csv('../datasets/fear.csv')
    df_joy = pd.read_csv('../datasets/joy.csv')
    df_surprise = pd.read_csv('../datasets/surprise.csv')
    df_love = pd.read_csv('../datasets/love.csv')
    data_set = [df_anger, df_fear, df_joy, df_surprise, df_love]

    data = pd.concat(data_set)

    X = data['Text']
    y = data['Emotion']

    X_train, X_test, y_train, y_test = train_test_split(
        X, 
        y, 
        test_size=0.2, 
        random_state=42
    )

    vect = CountVectorizer(
        tokenizer=preprocess_and_tokenize, 
        ngram_range=(1,2)
    )

    print("Training")
    # fit on our complete corpus
    vect.fit_transform(data.Text)
    # transform testing and training datasets to vectors
    X_train_vect = vect.transform(X_train)
    X_test_vect = vect.transform(X_test)

    model = LogisticRegression(
        multi_class='multinomial',
        class_weight='balanced', 
        solver='lbfgs', 
        max_iter=10000, 
        penalty='l2', 
        n_jobs=-1
    )

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