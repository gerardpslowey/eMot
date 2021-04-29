import time

import ktrain  # pip install ktrain, use ktrain as a lightweight wrapper, for deep learning in TensorFlow Keras
import pandas as pd
from ktrain import text
from sklearn.model_selection import train_test_split

from utils.textMod import spellCheck


def main():
    print("Loading Data Sets")
    df_anger = pd.read_csv("../datasets/anger.csv")
    df_fear = pd.read_csv("../datasets/fear.csv")
    df_joy = pd.read_csv("../datasets/joy.csv")
    df_surprise = pd.read_csv("../datasets/surprise.csv")
    df_happiness = pd.read_csv("../datasets/happiness.csv")
    df_sadness = pd.read_csv("../datasets/sadness.csv")

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

    class_names = ["anger", "fear", "joy", "surprise", "happiness", "sadness"]

    encoding = {
        "anger": 0,
        "fear": 1,
        "joy": 2,
        "surprise": 3,
        "happiness": 4,
        "sadness": 5,
    }

    # Integer values for each class
    y_train = [encoding[x] for x in y_train]
    y_test = [encoding[x] for x in y_test]

    (x_train, y_train), (x_test, y_test), preproc = text.texts_from_array(
        x_train=X_train,
        y_train=y_train,
        x_test=X_test,
        y_test=y_test,
        class_names=class_names,
        preprocess_mode="bert",
        maxlen=350,
        max_features=35000,
    )

    model = text.text_classifier(
        "bert", train_data=(
            x_train, y_train), preproc=preproc)

    learner = ktrain.get_learner(
        model, train_data=(
            x_train, y_train), val_data=(
            x_test, y_test), batch_size=6
    )

    learner.fit_onecycle(2e-5, 3)

    learner.validate(val_data=(x_test, y_test), class_names=class_names)

    predictor = ktrain.get_predictor(learner.model, preproc)
    predictor.get_classes()

    predictor.save("../models/bert_model")


def test():
    predictor = ktrain.load_predictor("../models/bert_model")

    message = "I just broke up with my girlfriend"

    startTime = time.time()
    prediction = predictor.predict(message)
    endTime = time.time()

    print("prediction: {} ({:.2f})".format(prediction, (endTime - startTime)))
