# Dataset handling
import sys
from pathlib import Path

import pandas as pd
# plots and metrics
from modelFuncs import plot_confusion_matrix, saveFiles
from sklearn.calibration import CalibratedClassifierCV
# feature extraction / vectorization
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
# classifiers
from sklearn.svm import LinearSVC
from tqdm import tqdm

from utils.textMod import preprocessAndTokenise, spellCheck

# sets path to src
sys.path.append(str(Path(__file__).parent.parent.absolute()))

tqdm.pandas()


def main():
    print("Loading Data Sets")
    df_anger = pd.read_csv("../datasets/anger.csv").astype("U")
    df_fear = pd.read_csv("../datasets/fear.csv").astype("U")
    df_joy = pd.read_csv("../datasets/joy.csv").astype("U")
    df_surprise = pd.read_csv("../datasets/surprise.csv").astype("U")
    df_happiness = pd.read_csv("../datasets/happiness.csv").astype("U")
    df_sadness = pd.read_csv("../datasets/sadness.csv").astype("U")

    data_set = [
        df_anger,
        df_fear,
        df_joy,
        df_surprise,
        df_happiness,
        df_sadness]

    data = pd.concat(data_set)

    print("\nChecking Spelling:")
    data["Text"] = data["Text"].progress_apply(spellCheck)

    X = data["Text"]
    y = data["Emotion"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("size of training set: %s" % (len(X_train)))
    print("size of validation set: %s" % (len(X_test)))
    # print(data.Emotion.value_counts())

    # TFIDF, unigrams and bigrams
    vect = TfidfVectorizer(
        tokenizer=preprocessAndTokenise, sublinear_tf=True, norm="l2", ngram_range=(1, 2)
    )

    print("Training")
    # fit on our complete corpus
    vect.fit_transform(data.Text)
    # transform testing and training datasets to vectors
    X_train_vect = vect.transform(X_train)
    X_test_vect = vect.transform(X_test)

    lsvc = LinearSVC(
        max_iter=10000,
        penalty="l2",
        loss="hinge",
        random_state=42,
        class_weight="balanced",
    )

    # used to get classification score
    clf = CalibratedClassifierCV(lsvc)
    clf.fit(X_train_vect, y_train)

    ysvm_pred = clf.predict(X_test_vect)
    print("Accuracy: {:.2f}%".format(accuracy_score(y_test, ysvm_pred) * 100))
    print(
        "F1 Score: {:.2f}".format(
            f1_score(
                y_test,
                ysvm_pred,
                average="micro") * 100)
    )

    class_names = ["anger", "fear", "joy", "surprise", "happiness", "sadness"]
    _, plt = plot_confusion_matrix(
        y_test,
        ysvm_pred,
        classes=class_names,
        normalize=True,
        title="Normalized confusion matrix",
    )

    plt.show()

    model_filename = "svc.pkl"
    tfidf_filename = "svc_tfidf.pkl"
    saveFiles(clf, model_filename)
    saveFiles(vect, tfidf_filename)
    print("Model and Data Saved")


if __name__ == "__main__":
    main()
