import pickle
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.absolute())) 

LR_Model = "models/lr.pkl"
LR_CV_File = "models/lr_cv.pkl"

SGD_Model = "models/sgd.pkl"
SGD_CV_File = "models/sgd_cv.pkl"

SVC_Model = "models/svc.pkl"
SVC_TFIDF_File = "models/svc_tfidf.pkl"

# def test_sentiment():    
#     model = loadFiles(LR_Model)
#     cv = loadFiles(LR_CV_File)

#     message = "This move is good and cool"
#     sentiment_value = model.predict(cv.transform([message]))[0]
#     # print(sentiment_value)

#     assert sentiment_value == 'joy'

# def test_sentiment2():    
#     model = loadFiles(SGD_Model)
#     cv = loadFiles(SGD_CV_File)

#     message = "this is horrible"
#     sentiment_value = model.predict(cv.transform([message]))
#     print(sentiment_value)

    # assert sentiment_value != 'love'

def test_sentiment3(): 
    model = loadFiles(SVC_Model)
    tfidf = loadFiles(SVC_TFIDF_File)

    reviews = ["my dog died", 
        "the car drove very fast before crashing",
        "pizza was hour late and my pizza is cold", 
        "it was a lovely sunny day today", 
        "vaccines are in the news",
        "this film is very good",
        "I had a brilliant birthday party"
    ]
    
    for review in reviews:
        sentiment_score = model.predict_proba(tfidf.transform([review]))
        sentiment_name = model.predict(tfidf.transform([review]))

        print(sentiment_score, sentiment_name)

    # assert sentiment_value == 'anger'

    # listOfScores = list(model.predict_proba(cv.transform([review])).flatten())
    # assert len(listOfScores)  <= len(review.split())

def loadFiles(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

if __name__ == "__main__":
    # test_sentiment()
    # test_sentiment2()
    test_sentiment3()