import pickle
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.absolute())) 

LR_Model = "models/lr.pkl"
LR_CV_File = "models/lr_cv.pkl"

SGD_Model = "models/sgd.pkl"
SGD_CV_File = "models/sgd_cv.pkl"

SVM_Model = "models/svm.pkl"
SGD_TFIDF_File = "models/svm_tfidf.pkl"


def test_sentiment():    
    model = loadFiles(LR_Model)
    cv = loadFiles(LR_CV_File)

    message = "This move is good and cool"
    sentiment_value = model.predict(cv.transform([message]))[0]
    # print(sentiment_value)

    assert sentiment_value == 'joy'

def test_sentiment2():    
    model = loadFiles(SGD_Model)
    cv = loadFiles(SGD_CV_File)

    message = "this is horrible"
    sentiment_value = model.predict(cv.transform([message]))[0]
    # print(sentiment_value)

    assert sentiment_value != 'love'

def test_sentiment3(): 
    model = loadFiles(SVM_Model)
    tfidf = loadFiles(SGD_TFIDF_File)

    review = "pizza was hour late and my pizza is cold"
    sentiment_value = model.predict(tfidf.transform([review]))[0]    
    # print(sentiment_value)

    assert sentiment_value == 'anger'

    # listOfScores = list(model.predict_proba(cv.transform([review])).flatten())
    # assert len(listOfScores)  <= len(review.split())

def loadFiles(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

if __name__ == "__main__":
    test_sentiment()
    test_sentiment2()
    test_sentiment3()