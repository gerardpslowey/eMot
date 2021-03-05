import pickle
from sklearn.feature_extraction.text import CountVectorizer

# TODO finish implementing this
def testSentiment(cv, model):    
    reviews = ["This move is good and cool", 
    "very nice very cool, king of the castle, king of the castle, I have a chair",
    "coronavirus has caused major turmoil recently"]

    for review in reviews:
        print(model.predict(cv.transform([review])))

def main():
    cv = CountVectorizer()

    pkl_filename = "pickle_model.pkl"
    with open(pkl_filename, 'rb') as file:
        pickle_model = pickle.load(file)

    testSentiment(cv, pickle_model)

if __name__ == '__main__':
    main()