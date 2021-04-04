# Dataset handling
import pandas as pd

# plots and metrics
from check_train import plot_confusion_matrix
from sklearn.metrics import accuracy_score, f1_score
from sklearn.calibration import CalibratedClassifierCV
from sklearn.model_selection import train_test_split

# feature extraction / vectorization
from sklearn.feature_extraction.text import TfidfVectorizer

# classifiers
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline

# save and load a file
import pickle

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.absolute())) 
from urlProcessor.textMod import preprocess_and_tokenize, saveFiles, spellCheck, removeRepetitions

from tqdm import tqdm
tqdm.pandas()


def main():
    print("Loading Data Sets")
    df_anger = pd.read_csv('../datasets/anger.csv')
    df_fear = pd.read_csv('../datasets/fear.csv')
    df_joy = pd.read_csv('../datasets/joy.csv')
    df_surprise = pd.read_csv('../datasets/surprise.csv')

    df_happiness = pd.read_csv('../datasets/happiness.csv')
    df_happiness = df_happiness.sample(n=5000)

    data_set = [df_anger, df_fear, df_joy, df_surprise, df_happiness]

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

    print('size of training set: %s' % (len(X_train)))
    print('size of validation set: %s' % (len(X_test)))
    # print(data.Emotion.value_counts())

    # TFIDF, unigrams and bigrams
    vect = TfidfVectorizer(
        tokenizer=preprocess_and_tokenize, 
        sublinear_tf=True, 
        norm='l2', 
        ngram_range=(1,2)
    )

    print("Training")
    # fit on our complete corpus
    vect.fit_transform(data.Text)
    # transform testing and training datasets to vectors
    X_train_vect = vect.transform(X_train)
    X_test_vect = vect.transform(X_test)

    lsvc = LinearSVC(
        tol=1e-05, 
        max_iter=10000,
        penalty='l2',
        loss='hinge',
        random_state=42,
        class_weight='balanced',
    )

    clf = CalibratedClassifierCV(lsvc) 
    clf.fit(X_train_vect, y_train)

    ysvm_pred = clf.predict(X_test_vect)
    print("Accuracy: {:.2f}%".format(accuracy_score(y_test, ysvm_pred) * 100))
    print("F1 Score: {:.2f}".format(f1_score(y_test, ysvm_pred, average='micro') * 100))

    class_names = ['anger', 'fear', 'joy', 'surprise', 'happiness']
    _, plt = plot_confusion_matrix(
        y_test, 
        ysvm_pred, 
        classes=class_names, 
        normalize=True, 
        title='Normalized confusion matrix'
    )

    plt.show()

    model_filename = 'svc.pkl'
    tfidf_filename = 'svc_tfidf.pkl'
    saveFiles(clf, model_filename)
    saveFiles(vect, tfidf_filename)
    print("Model and Data Saved")



if __name__ == '__main__':
    main()