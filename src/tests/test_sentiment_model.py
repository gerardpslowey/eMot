import pickle
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.absolute())) 

CV_LR_Model = "models/cv_lr.pkl"
CV_SGD_Model = "models/cv_sgd.pkl"
TFIDF_SVM_Model = "models/tfidf_svm.pkl"

def test_sentiment():    
    model = loadFiles(CV_LR_Model)
    message = "This move is good and cool"
    assert model.predict([message]) == 'joy'

def test_sentiment2():    
    model = loadFiles(CV_SGD_Model)

    message = "this is horrible"
    sentiment_value = model.predict([message])
    assert sentiment_value != 'love'

def test_sentiment3(): 
    model = loadFiles(TFIDF_SVM_Model)
    
    review = "pizza was hour late and my pizza is cold"
    sentiment_value = model.predict([review])
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