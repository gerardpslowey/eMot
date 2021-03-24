import pickle

emotions_dict = {0:"neutral", 1:"worry", 2:"happiness", 3:"sadness", 4:"love", 5:"surprise", 6:"fun", 7:"relief", 8:"hate", 9:"empty", 10:"enthusiasm", 11:"boredom", 12:"anger"}
model_filename = "../models/LRModelEmotion.pkl"
cv_filename = "../models/CVFileEmotions.pkl"

def test_sentiment():    
    model = loadFiles(model_filename)
    cv = loadFiles(cv_filename)

    review = "This move is good and cool"
    sentiment_value = model.predict(cv.transform([review]))[0]
    assert emotions_dict[sentiment_value] == 'happiness'

def test_sentiment2():    
    model = loadFiles(model_filename)
    cv = loadFiles(cv_filename)

    review = "this is tragic"
    sentiment_value = model.predict(cv.transform([review]))[0]
    assert emotions_dict[sentiment_value] != 'love'

def test_sentiment3(): 
    model = loadFiles(model_filename)
    cv = loadFiles(cv_filename) 
    
    review = "very nice very cool, king of the castle, king of the castle, I have a chair"
    listOfScores = list(model.predict_proba(cv.transform([review])).flatten())
    assert len(listOfScores)  <= len(review.split())

def loadFiles(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)