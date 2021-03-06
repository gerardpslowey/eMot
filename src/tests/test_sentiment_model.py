import pickle
import sys
from pathlib import Path

# sets path to src
sys.path.append(str(Path(__file__).parent.parent.absolute()))

LR_Model = "models/lr.pkl"
LR_CV_File = "models/lr_cv.pkl"

SGD_Model = "models/sgd.pkl"
SGD_CV_File = "models/sgd_cv.pkl"

SVC_Model = "models/svc.pkl"
SVC_TFIDF_File = "models/svc_tfidf.pkl"


def test_sentiment():
    model = loadFiles(LR_Model)
    cv = loadFiles(LR_CV_File)

    message = "The weather is to remain dull with rain to come"
    sentiment_value = model.predict(cv.transform([message]))[0]

    assert sentiment_value != "sadness"


def test_sentiment2():
    model = loadFiles(SGD_Model)
    cv = loadFiles(SGD_CV_File)

    message = "this is horrible"
    sentiment_value = model.predict(cv.transform([message]))

    assert sentiment_value != "joy"


def test_happiness_sentiment():
    model = loadFiles(SVC_Model)
    tfidf = loadFiles(SVC_TFIDF_File)

    reviews = [
        "it was a lovely sunny day today",
        "this film is very good",
        "he's the nicest guy I know",
    ]

    for review in reviews:
        sentiment_name = model.predict(tfidf.transform([review]))
        assert sentiment_name == "happiness"


def test_sadness_sentiment():
    model = loadFiles(SVC_Model)
    tfidf = loadFiles(SVC_TFIDF_File)
    sentence = "my dog died"
    sentiment_name = model.predict(tfidf.transform([sentence]))
    assert sentiment_name == "sadness"


def loadFiles(filename):
    with open(filename, "rb") as file:
        return pickle.load(file)
