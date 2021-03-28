import pandas as pd, pickle
from tqdm import tqdm
tqdm.pandas()

from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, f1_score
from sklearn.pipeline import Pipeline

# filter warning about using custom tokenizer
import warnings
warnings.filterwarnings('ignore') 

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.absolute())) 
from urlProcessor.textMod import preprocess_and_tokenize, saveFiles

def main():
    # read the dataset into a data frame
    df_train = pd.read_csv('../datasets/data_train.csv')
    df_test = pd.read_csv('../datasets/data_test.csv')

    X_train = df_train.Text
    x_test = df_test.Text

    y_train = df_train.Emotion
    y_test = df_test.Emotion

    data = pd.concat([df_train, df_test])

    cv = CountVectorizer(tokenizer=preprocess_and_tokenize, ngram_range=(1,2))
    cv.fit(data['Text'])
    X_train_count = cv.transform(X_train)
    x_test_count = cv.transform(x_test)

    #alpha = loss checker
    sgd = SGDClassifier(alpha=0.001, loss='modified_huber', penalty='l2', tol=None, n_jobs=-1)
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