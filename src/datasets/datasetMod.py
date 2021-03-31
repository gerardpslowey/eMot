import pandas as pd
import sys, csv
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.absolute())) 

def modifyDailydialog():
    df = pd.read_csv('dailydialog/dailydialog_all.csv')

    df['Emotion'] = df['Emotion'].apply(customSentiment)

    grouped = df.groupby(df.Emotion)

    neutral = grouped.get_group("neutral")
    anger = grouped.get_group("anger")
    disgust = grouped.get_group("disgust")
    fear = grouped.get_group("fear")
    happiness = grouped.get_group("happiness")
    surprise = grouped.get_group("surprise")

    neutral.to_csv('dailydialog_neutral.csv', index=False, encoding='utf-8')
    anger.to_csv('dailydialog_anger.csv', index=False, encoding='utf-8')
    disgust.to_csv('dailydialog_disgust.csv', index=False, encoding='utf-8')
    fear.to_csv('dailydialog_fear.csv', index=False, encoding='utf-8')
    happiness.to_csv('dailydialog_hapiness.csv', index=False, encoding='utf-8')
    surprise.to_csv('dailydialog_surprise.csv', index=False, encoding='utf-8')

def modEmoint():
    df = pd.read_csv('emoint/emoint_all.csv', delimiter="\t", header=None)
    # drop unused columns
    df = df.drop(df.columns[[0, 3]], axis=1)

    # swap column order
    df = df[[2, 1]]

    print(df[2].value_counts())
    df.columns=["Emotion", "Text"]
    grouped = df.groupby(df['Emotion'])

    fear = grouped.get_group("fear")
    anger = grouped.get_group("anger")
    joy = grouped.get_group("joy")
    sadness = grouped.get_group("sadness")

    fear.to_csv('emoint/emoint_fear.csv', index=False, encoding='utf-8')
    anger.to_csv('emoint/emoint_anger.csv', index=False, encoding='utf-8')
    joy.to_csv('emoint/emoint_joy.csv', index=False, encoding='utf-8')
    sadness.to_csv('emoint/emoint_sadness.csv', index=False, encoding='utf-8')

def modTextEmotion():
    df = pd.read_csv('text_emotion/emotion_all.csv', delimiter=",")
    # drop unused columns
    df = df.drop(df.columns[[0, 2]], axis=1)
    df = df[['sentiment', 'content']]

    # print(df.head())
    # print(df['sentiment'].value_counts())

    df.columns=['Emotion', 'Text']
    grouped = df.groupby(df['Emotion'])

    neutral = grouped.get_group("neutral")
    worry = grouped.get_group("worry")
    happiness = grouped.get_group("happiness")
    sadness = grouped.get_group("sadness")
    love = grouped.get_group("love")
    surprise = grouped.get_group("surprise")
    fun = grouped.get_group("fun")
    relief = grouped.get_group("relief")
    hate = grouped.get_group("hate")
    empty = grouped.get_group("empty")
    enthusiasm = grouped.get_group("enthusiasm")
    boredom = grouped.get_group("boredom")
    anger = grouped.get_group("anger")

    neutral.to_csv('text_emotion/emotion_neutral.csv', index=False, encoding='utf-8')
    worry.to_csv('text_emotion/emotion_worry.csv', index=False, encoding='utf-8')
    happiness.to_csv('text_emotion/emotion_happiness.csv', index=False, encoding='utf-8')
    sadness.to_csv('text_emotion/emotion_sadness.csv', index=False, encoding='utf-8')
    love.to_csv('text_emotion/emotion_love.csv', index=False, encoding='utf-8')
    surprise.to_csv('text_emotion/emotion_surprise.csv', index=False, encoding='utf-8')
    fun.to_csv('text_emotion/emotion_fun.csv', index=False, encoding='utf-8')
    relief.to_csv('text_emotion/emotion_relief.csv', index=False, encoding='utf-8')
    hate.to_csv('text_emotion/emotion_hate.csv', index=False, encoding='utf-8')
    empty.to_csv('text_emotion/emotion_empty.csv', index=False, encoding='utf-8')
    enthusiasm.to_csv('text_emotion/emotion_enthusiasm.csv', index=False, encoding='utf-8')
    boredom.to_csv('text_emotion/emotion_boredom.csv', index=False, encoding='utf-8')
    anger.to_csv('text_emotion/emotion_anger.csv', index=False, encoding='utf-8')


def customSentiment(sentiment):
    if sentiment == 0:
        return "neutral"
    elif sentiment == 1:
        return "anger"
    elif sentiment == 2:
        return "disgust"
    elif sentiment == 3:
        return "fear"
    elif sentiment == 4:
        return "happiness"
    elif sentiment == 5:
        return "sadness"
    elif sentiment == 6:
        return "surprise"

if __name__ == "__main__":
    modifyDailydialog()
    modEmoint()
    modTextEmotion()
