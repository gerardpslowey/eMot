# Dataset handling
import pandas as pd

# plots and metrics
import matplotlib.pyplot as plt, numpy as np
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
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
from urlProcessor.textMod import preprocess_and_tokenize, saveFiles

def main():
    df_anger = pd.read_csv('anger.csv')
    df_fear = pd.read_csv('fear.csv')
    df_joy = pd.read_csv('joy.csv')
    df_surprise = pd.read_csv('surprise.csv')
    df_love = pd.read_csv('love.csv')
    data_set = [df_anger, df_fear, df_joy, df_surprise, df_love]

    data = pd.concat(data_set)

    X = data['Text']
    y = data['Emotion']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

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
        penalty='l2',
        loss='hinge',
        random_state=42,
        class_weight='balanced'
    )

    clf = CalibratedClassifierCV(lsvc) 
    clf.fit(X_train_vect, y_train)

    ysvm_pred = clf.predict(X_test_vect)
    print("Accuracy: {:.2f}%".format(accuracy_score(y_test, ysvm_pred) * 100))
    print("F1 Score: {:.2f}".format(f1_score(y_test, ysvm_pred, average='micro') * 100))
    print("\nConfusion Matrix:\n", confusion_matrix(y_test, ysvm_pred))

    class_names = ['anger', 'fear', 'joy', 'surprise', 'love']
    plot_confusion_matrix(y_test, ysvm_pred, classes=class_names, normalize=True, title='Normalized confusion matrix')
    plt.show()

    # model_filename = 'svc.pkl'
    # tfidf_filename = 'svc_tfidf.pkl'
    # saveFiles(clf, model_filename)
    # saveFiles(vect, tfidf_filename)

def plot_confusion_matrix(y_true, y_pred, classes, normalize=False, title=None, cmap=plt.cm.Blues):
    # This function prints and plots the confusion matrix.
    # Normalization can be applied by setting `normalize=True`.
    if not title:
        if normalize:
            title = 'Normalized confusion matrix'
        else:
            title = 'Confusion matrix, without normalization'

    # Compute confusion matrix
    cm = confusion_matrix(y_true, y_pred)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

    fig, ax = plt.subplots()
    
    # Set size
    fig.set_size_inches(12.5, 7.5)
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)
    ax.grid(False)
    
    # We want to show all ticks...
    ax.set(xticks = np.arange(cm.shape[1]),
           yticks = np.arange(cm.shape[0]),
           # ... and label them with the respective list entries
           xticklabels = classes, yticklabels=classes,
           title = title,
           ylabel ='True label',
           xlabel ='Predicted label')

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], fmt),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()
    return ax

if __name__ == '__main__':
    main()