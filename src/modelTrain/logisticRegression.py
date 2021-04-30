import sys
from pathlib import Path

import pandas as pd
from modelFuncs import saveFiles
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from tqdm import tqdm

from utils.textMod import preprocessAndTokenise, spellCheck

tqdm.pandas()

# sets path to src
sys.path.append(str(Path(__file__).parent.parent.absolute()))


def main():
    print("Loading Data Sets")
    df_anger = pd.read_csv("../datasets/anger.csv").astype("U")
    df_fear = pd.read_csv("../datasets/fear.csv").astype("U")
    df_joy = pd.read_csv("../datasets/joy.csv").astype("U")
    df_surprise = pd.read_csv("../datasets/surprise.csv").astype("U")

    df_happiness = pd.read_csv("../datasets/happiness.csv").astype("U")
    df_happiness = df_happiness.sample(n=5000)

    df_sadness = pd.read_csv("../datasets/sadness.csv").astype("U")
    df_sadness = df_sadness.sample(n=5000)

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

    vect = CountVectorizer(tokenizer=preprocessAndTokenise, ngram_range=(1, 2))

    print("Training")
    # fit on our complete corpus
    vect.fit_transform(data.Text)
    # transform testing and training datasets to vectors
    X_train_vect = vect.transform(X_train)
    X_test_vect = vect.transform(X_test)

    model = LogisticRegression(
        multi_class="multinomial",
        class_weight="balanced",
        solver="lbfgs",
        max_iter=10000,
        penalty="l2",
        n_jobs=-1,
    )

    model.fit(X_train_vect, y_train)

    y_pred = model.predict(X_test_vect)
    print("Accuracy: {:.2f}%".format(accuracy_score(y_test, y_pred) * 100))
    print(
        "F1 Score: {:.2f}".format(
            f1_score(
                y_test,
                y_pred,
                average="micro") *
            100))

    model_filename = "lr.pkl"
    cv_filename = "lr_cv.pkl"
    saveFiles(model, model_filename)
    saveFiles(vect, cv_filename)


if __name__ == "__main__":
    main()
