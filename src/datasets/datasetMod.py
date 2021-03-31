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

    neutral.to_csv('dailydialog/dailydialog_neutral.csv', index=False, encoding='utf-8')
    anger.to_csv('dailydialog/dailydialog_anger.csv', index=False, encoding='utf-8')
    disgust.to_csv('dailydialog/dailydialog_disgust.csv', index=False, encoding='utf-8')
    fear.to_csv('dailydialog/dailydialog_fear.csv', index=False, encoding='utf-8')
    happiness.to_csv('dailydialog/dailydialog_happiness.csv', index=False, encoding='utf-8')
    surprise.to_csv('dailydialog/dailydialog_surprise.csv', index=False, encoding='utf-8')

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

def modIsear():
    df = pd.read_csv('isear/isear_all.csv', delimiter=",")

    # print(df['Emotion'].value_counts())

    grouped = df.groupby(df['Emotion'])

    joy = grouped.get_group("joy")
    sadness = grouped.get_group("sadness")
    anger = grouped.get_group("anger")
    neutral = grouped.get_group("neutral")
    fear = grouped.get_group("fear")
   
    joy.to_csv('isear/isear_joy.csv', index=False, encoding='utf-8')
    sadness.to_csv('isear/isear_sadness.csv', index=False, encoding='utf-8')
    anger.to_csv('isear/isear_anger.csv', index=False, encoding='utf-8')
    neutral.to_csv('isear/isear_neutral.csv', index=False, encoding='utf-8')
    fear.to_csv('isear/isear_fear.csv', index=False, encoding='utf-8')

def concatEmotions():
    # ANGER
    df_anger_1 = pd.read_csv('dailydialog/dailydialog_anger.csv', delimiter=",")
    df_anger_2 = pd.read_csv('emoint/emoint_anger.csv', delimiter=",")
    df_anger_3 = pd.read_csv('isear/isear_anger.csv', delimiter=",")
    df_anger_4 = pd.read_csv('text_emotion/emotion_anger.csv', delimiter=",")

    anger_list = [df_anger_1, df_anger_2, df_anger_3, df_anger_4]
    df_anger = pd.concat(anger_list)
    # Drop any duplicates
    df_anger.drop_duplicates()
    # print(df.shape)
    # 5092 Anger
    df_anger.to_csv('anger.csv', index=False, encoding='utf-8')

    
    # FEAR
    df_fear_1 = pd.read_csv('dailydialog/dailydialog_fear.csv', delimiter=",")
    df_fear_2 = pd.read_csv('emoint/emoint_fear.csv', delimiter=",")
    df_fear_3 = pd.read_csv('isear/isear_fear.csv', delimiter=",")

    fear_list = [df_fear_1, df_fear_2, df_fear_3]
    df_fear = pd.concat(fear_list)
    # Drop any duplicates
    df_fear.drop_duplicates()
    # print(df_fear.shape)
    # 4597 Fear
    df_fear.to_csv('fear.csv', index=False, encoding='utf-8')


    # JOY
    df_joy_1 = pd.read_csv('emoint/emoint_joy.csv', delimiter=",")
    df_joy_2 = pd.read_csv('isear/isear_joy.csv', delimiter=",")

    joy_list = [df_joy_1, df_joy_2]
    df_joy = pd.concat(joy_list)
    # Drop any duplicates
    df_joy.drop_duplicates()
    # print(df_joy.shape)
    # 3942 Joy
    df_joy.to_csv('joy.csv', index=False, encoding='utf-8')


    # SADNESS
    df_sadness_1 = pd.read_csv('emoint/emoint_sadness.csv', delimiter=",")
    df_sadness_2 = pd.read_csv('isear/isear_sadness.csv', delimiter=",")
    df_sadness_3 = pd.read_csv('text_emotion/emotion_sadness.csv', delimiter=",")

    sadness_list = [df_sadness_1, df_sadness_2, df_sadness_3]
    df_sadness = pd.concat(sadness_list)
    # Drop any duplicates
    df_sadness.drop_duplicates()
    # print(df.shape)
    # 9015 Sadness
    df_sadness.to_csv('sadness.csv', index=False, encoding='utf-8')


    # NEUTRAL
    df_neutral_1 = pd.read_csv('dailydialog/dailydialog_neutral.csv', delimiter=",")
    df_neutral_3 = pd.read_csv('isear/isear_neutral.csv', delimiter=",")
    df_neutral_4 = pd.read_csv('text_emotion/emotion_neutral.csv', delimiter=",")

    neutral_list = [df_neutral_1, df_neutral_3, df_neutral_4]
    df_neutral = pd.concat(neutral_list)
    # Drop any duplicates
    df_neutral.drop_duplicates()
    # print(df_neutral.shape)
    # 96464 Neutral
    df_neutral.to_csv('neutral.csv', index=False, encoding='utf-8')


    # HAPPINESS
    df_happiness_1 = pd.read_csv('dailydialog/dailydialog_happiness.csv', delimiter=",")
    df_happiness_4 = pd.read_csv('text_emotion/emotion_happiness.csv', delimiter=",")

    happiness_list = [df_happiness_1, df_happiness_4]
    df_happiness = pd.concat(happiness_list)
    # Drop any duplicates
    df_happiness.drop_duplicates()
    # print(df_happiness.shape)
    # 18094 Happiness
    df_happiness.to_csv('happiness.csv', index=False, encoding='utf-8')


    # SURPRISE
    df_surprise_1 = pd.read_csv('dailydialog/dailydialog_surprise.csv', delimiter=",")
    df_surprise_4 = pd.read_csv('text_emotion/emotion_surprise.csv', delimiter=",")

    surprise_list = [df_surprise_1, df_surprise_4]
    df_surprise = pd.concat(surprise_list)
    # Drop any duplicates
    df_surprise.drop_duplicates()
    # print(df_surprise.shape)
    # 4010 Surprise
    df_surprise.to_csv('surprise.csv', index=False, encoding='utf-8')


    # WORRY
    df_worry = pd.read_csv('text_emotion/emotion_worry.csv', delimiter=",")
    # Drop any duplicates
    df_worry.drop_duplicates()
    # print(df_worry.shape)
    # 8459 worry
    df_worry.to_csv('worry.csv', index=False, encoding='utf-8')


    # LOVE
    df_love = pd.read_csv('text_emotion/emotion_love.csv', delimiter=",")

    # Drop any duplicates
    df_love.drop_duplicates()
    # print(df_love.shape)
    # 4010 love
    df_love.to_csv('love.csv', index=False, encoding='utf-8')

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
    # modifyDailydialog()
    # modEmoint()
    # modTextEmotion()
    # modIsear()
    concatEmotions()
