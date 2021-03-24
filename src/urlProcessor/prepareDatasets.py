import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.absolute())) 
from urlProcessor.textMod import saveFiles, preProcess, removeURLs, removeRepetitions, spellCheck, wordcloud_draw

from multiprocessing import  Pool

import pandas as pd

from tqdm import tqdm
tqdm.pandas()

def main():
    # cleanBinomialDataset("../datasets/train.csv")
    cleanEmotionDataset("../datasets/text_emotion.csv")

def cleanBinomialDataset(dataset):
    print("Reading Training Data")
    trainSet = pd.read_csv(dataset)
    print("Finished Reading")

    print("\nCleaning Binomial Data Set")
    trainSet['CustomSentiment'] = trainSet.progress_apply(lambda x: customSentiment(x['Sentiment']), axis=1)
    trainSet['Tweet'] = trainSet['Tweet'].progress_apply(preProcess)
    trainSet['Tweet'] = trainSet['Tweet'].progress_apply(removeURLs)
    trainSet['Tweet'] = trainSet['Tweet'].progress_apply(removeRepetitions)
    trainSet['Tweet'] = trainSet['Tweet'].progress_apply(spellCheck)
    print("Finished Cleaning")

    trainSet.to_csv('../datasets/train_cleaned.csv', index=False)
    print("Saved to File")

def cleanEmotionDataset(dataset):
    print("Reading Training Data")
    df = pd.read_csv(dataset)
    print("Finished Reading")

    print("\nCleaning Data Set")
    df['content'] = df['content'].progress_apply(preProcess)
    df['content'] = df['content'].progress_apply(removeURLs)
    df['content'] = df['content'].progress_apply(removeRepetitions)
    df['content'] = df['content'].progress_apply(spellCheck)

    df.to_csv('../datasets/text_emotion_cleaned.csv', index=False)
    print("Saved to File")

def customSentiment(sentiment):
    if sentiment == "neg":
        return 0  
    elif sentiment == "pos":
        return 1
    else:
        return 2

if __name__ == '__main__':
    main()