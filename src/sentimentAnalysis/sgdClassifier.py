import pandas as pd  # , pickle
from tqdm import tqdm
tqdm.pandas()

from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split

# filter warning about using custom tokenizer
import warnings
warnings.filterwarnings('ignore')

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.absolute()))
from utils.textMod import saveFiles, spellCheck, preprocessAndTokenise
# from utils.textMod import preProcess


def main():
    print("Loading Data Sets")
    df_anger = pd.read_csv('../datasets/anger.csv')
    df_fear = pd.read_csv('../datasets/fear.csv')
    df_joy = pd.read_csv('../datasets/joy.csv')
    df_surprise = pd.read_csv('../datasets/surprise.csv')

    df_happiness = pd.read_csv('../datasets/happiness.csv')
    df_happiness = df_happiness.sample(n=5000)

    df_sadness = pd.read_csv('../datasets/sadness.csv')
    df_sadness = df_sadness.sample(n=5000)

    data_set = [df_anger, df_fear, df_joy, df_surprise, df_happiness, df_sadness]

    data = pd.concat(data_set)

    print("\nChecking Spelling:")
    data['Text'] = data['Text'].progress_apply(spellCheck)

    X = data['Text']
    y = data['Emotion']

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    cv = CountVectorizer(
        tokenizer=preprocessAndTokenise,
        ngram_range=(1, 2)
    )

    X_train_count = cv.fit_transform(X_train)
    x_test_count = cv.transform(X_test)

    sgd = SGDClassifier(
        alpha=0.001,
        loss='modified_huber',
        penalty='l2',
        tol=None,
        n_jobs=-1
    )

    sgd.fit(X_train_count, y_train)
    ysvm_pred = sgd.predict(x_test_count)
    print("Accuracy: {:.2f}%".format(accuracy_score(y_test, ysvm_pred) * 100))
    print("F1 Score: {:.2f}".format(f1_score(y_test, ysvm_pred, average='micro') * 100))

    model_filename = 'sgd.pkl'
    cv_filename = 'sgd_cv.pkl'
    saveFiles(sgd, model_filename)
    saveFiles(cv, cv_filename)


if __name__ == '__main__':
    main()
