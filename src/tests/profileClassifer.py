import time
import pickle

from pathlib import Path
import sys

# sets path to src
sys.path.append(str(Path(__file__).parent.parent.absolute()))

SVC_Model = "models/svc.pkl"
SVC_TFIDF_File = "models/svc_tfidf.pkl"


def profile_classifier():
    model = loadFiles(SVC_Model)
    tfidf = loadFiles(SVC_TFIDF_File)
    sentence = "inside traveller wedding as revellers dance and sing while gardai surround area"
    start_time = time.time()
    model.predict(tfidf.transform([sentence]))
    end_time = time.time()
    print(end_time - start_time)


def profile_classifier_2():
    model = loadFiles(SVC_Model)
    tfidf = loadFiles(SVC_TFIDF_File)
    sentence = "three injured during multi vehicle collision"
    start_time = time.time()
    model.predict(tfidf.transform([sentence]))
    end_time = time.time()
    print(end_time - start_time)


def loadFiles(filename):
    with open(filename, "rb") as file:
        return pickle.load(file)


if __name__ == '__main__':
    profile_classifier()
    profile_classifier_2()
