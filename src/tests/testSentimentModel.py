import pickle

def testSentiment(cv, model):    
    reviews = ["This move is good and cool", 
    "very nice very cool, king of the castle, king of the castle, I have a chair",
    "coronavirus has caused major turmoil recently", 
    "Eoghan mcDermott has left 2fm after six years following allegations of assault"]

    for review in reviews:
        print(model.predict(cv.transform([review])))

def loadFiles(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

def main():
    model_filename = "../LR_Model.pkl"
    cv_filename = "../CV_File.pkl"

    model = loadFiles(model_filename)
    cv = loadFiles(cv_filename)
    testSentiment(cv, model)

if __name__ == '__main__':
    main()