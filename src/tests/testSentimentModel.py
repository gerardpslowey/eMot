import pickle

sentiment_dictionary = {0:"Negative", 1:"Positive", 2:"Neutral"}
emotions_dict = {0:"neutral", 1:"worry", 2:"happiness", 3:"sadness", 4:"love", 5:"surprise", 6:"fun", 7:"relief", 8:"hate", 9:"empty", 10:"enthusiasm", 11:"boredom", 12:"anger"}

def testSentiment(cv, model):    
    reviews = ["This move is good and cool", 
    "very nice very cool, king of the castle, king of the castle, I have a chair",
    "coronavirus has caused major turmoil recently", 
    "Eoghan mcDermott has left 2fm after six years following allegations of assault",
    "this is tragic"]

    for review in reviews:
        sent_value = model.predict(cv.transform([review]))[0]
        print("{}: {}".format(model.predict_proba(cv.transform([review])), emotions_dict[sent_value]))


def loadFiles(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

def main():
    model_filename = "../models/LRModelEmotion.pkl"
    cv_filename = "../models/CVFileEmotions.pkl"
    model = loadFiles(model_filename)
    cv = loadFiles(cv_filename)
    testSentiment(cv, model)

if __name__ == '__main__':
    main()