import pandas as pd
import pickle
import threading
from utils.urlFilter import base
import copy

scrapedFile = 'sentimentAnalysis/scraped.csv'


class EmotClassify:
    def __init__(self):
        self.emotions = ['anger', 'fear', 'joy', 'surprise', 'happiness', 'sadness']
        # make a nested dictionary setting the emotion count values to zero
        self.emotions_dict = dict.fromkeys(self.emotions, 0)

        self.emotion_count = copy.deepcopy(self.emotions_dict)
        self.emotion_intensity = copy.deepcopy(self.emotions_dict)

        self.emotionsPerSiteDict = {}
        # self.emotionsPerSiteDict = OrderedDict()

        self.sentenceExamples = set()

        self.site_visit_counts = None
        self.total_sites = 0

        self.svc_model = "models/svc.pkl"
        self.svc_tfidf_file = "models/svc_tfidf.pkl"
        self.model_1 = self.loadFiles(self.svc_model)
        self.tfidf = self.loadFiles(self.svc_tfidf_file)

        # an empty array for line chart array values
        self.splitChartValues = []
        self.wordCloudBag = []

    # number of times a site is visited
    def siteCount(self):
        # only load the urls column from the file
        urls_df = pd.read_csv(scrapedFile, usecols=["url"]).astype('U')
        urls_df['base'] = urls_df['url'].apply(base)
        self.site_visit_counts = urls_df['base'].value_counts().to_dict()

        print("Articles read per site: ")
        self.prettyPrint(self.site_visit_counts.items())

    def sentenceClassify(self):
        scraped_df = pd.read_csv(scrapedFile).astype('U')

        scraped_df['base'] = scraped_df['url'].apply(base)
        # create a list of unique base sites
        sitesList = scraped_df['base'].unique().tolist()
        # create a nested dictionary for each site
        for site in sitesList:
            # dictionary key maps to a nested dictionary
            self.emotionsPerSiteDict[site] = copy.deepcopy(self.emotions_dict)

        try:
            for row in scraped_df.itertuples(index=False):
                text = row[1]
                url = row[2]

                # score each sentence
                for sentence in text.split("|"):
                    sentiment_score = self.model_1.predict_proba(self.tfidf.transform([sentence]))
                    sentiment_name = self.model_1.predict(self.tfidf.transform([sentence]))

                    emotion = sentiment_name[0]
                    intensity = sentiment_score.max()

                    if intensity >= 0.6:
                        # count total emotion count
                        self.emotion_count[emotion] += 1
                        # count of distribution of emotions per site
                        self.emotionsPerSiteDict[url][emotion] += 1

                        if intensity > self.emotion_intensity.get(emotion):
                            # round the intensity float to 2 decimal place
                            self.emotion_intensity[emotion] = round(intensity, 2)
                            self.wordCloudBag.append(sentence)
                            self.sentenceExamples.update([tuple((round(intensity, 2), emotion, sentence))])

            # total site visits = the number of sites visited
            self.total_sites = len(self.emotionsPerSiteDict)

            for _ in range(self.total_sites):
                for siteEmotionDict in self.emotionsPerSiteDict.values():
                    self.splitChartValues.append(list(siteEmotionDict.values()))

        except pd.errors.EmptyDataError:
            print("Nothing to classify, the file is empty")
        finally:
            print("\nThe Intensity level of each Emotion:")
            self.prettyPrint(self.emotion_intensity.items(), "percent")

            print("\nThe Amount of each Emotion:")
            self.prettyPrint(self.emotion_count.items())

            print("\nSites and associated article primary emotion: ")
            print(f"website: {*self.emotions,}")
            self.prettyPrint(self.emotionsPerSiteDict.items(), "lst")

            print("\nExamples of emotion based sentences: ")

            sentenceExampleList = list(self.sentenceExamples)
            sentenceExampleList.sort(key=lambda tup: tup[0], reverse=True)
            for item in sentenceExampleList[0:int(len(sentenceExampleList) / 2)]:
                print(f"{item[0]:.1%} {item[1]} = {item[2]}")

    def prettyPrint(self, items, format=None):
        for key, value in items:

            if format == "lst":
                print(f"{key}: {*list(value.values()),}")

            elif format == "percent":
                print(f"{key}: {value:.1%}")

            else:
                print(f"{key}: {value}")

    def loadFiles(self, filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)

    def get_emotions(self):
        return self.emotions

    def get_emotion_count(self):
        return self.emotion_count

    def get_emotion_intensity(self):
        return self.emotion_intensity

    def get_site_count(self):
        return self.site_visit_counts

    def get_total_sites(self):
        return self.total_sites

    def get_split_chart_values(self):
        return self.splitChartValues

    def get_wordcloud_bag(self):
        return self.wordCloudBag

    def startAll(self):
        threads = []
        process1 = threading.Thread(target=self.sentenceClassify)
        process1.start()
        threads.append(process1)

        process2 = threading.Thread(target=self.siteCount)
        process2.start()
        threads.append(process2)

        for process in threads:
            process.join()


if __name__ == '__main__':
    test = EmotClassify()
    test.startAll()
