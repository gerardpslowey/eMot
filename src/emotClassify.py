import pandas as pd
import pickle
import threading
from utils.urlFilter import base
import copy

scrapedFile = 'sentimentAnalysis/scraped.csv'


class EmotClassify:
    def __init__(self):
        self.emotions = ['anger', 'fear', 'joy', 'surprise', 'happiness', 'sadness']
        # make a nested dictionary setting the emotion_1 count values to zero
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
        self.sgd_model = "models/sgd.pkl"
        self.sgd_cv_file = "models/sgd_cv.pkl"

        self.model_1 = self.loadFiles(self.svc_model)
        self.tfidf = self.loadFiles(self.svc_tfidf_file)
        self.model_2 = self.loadFiles(self.sgd_model)
        self.cv = self.loadFiles(self.sgd_cv_file)

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
        # read scraped file
        scraped_df = pd.read_csv(scrapedFile).astype('U')
        # create a new column with the base url as its value
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
                    sentiment_score_1 = self.model_1.predict_proba(self.tfidf.transform([sentence]))
                    sentiment_score_2 = self.model_2.predict_proba(self.cv.transform([sentence]))

                    # use 2 models to score the data for comparison
                    intensity_1 = sentiment_score_1.max()
                    intensity_2 = sentiment_score_2.max()
                    intensity = (intensity_1 + intensity_2) / 2

                    sentiment_name_1 = self.model_1.predict(self.tfidf.transform([sentence]))
                    sentiment_name_2 = self.model_2.predict(self.cv.transform([sentence]))
                    emotion_1 = sentiment_name_1[0]
                    emotion_2 = sentiment_name_2[0]

                    # for a sentiment to be accepted both models have to have a score greater than 0.6
                    if intensity_1 >= 0.6 and intensity_2 >= 0.6 and emotion_1 == emotion_2:
                        # count total emotion count
                        self.emotion_count[emotion_1] += 1
                        # count of distribution of emotions per site
                        self.emotionsPerSiteDict[url][emotion_1] += 1

                    if intensity > self.emotion_intensity.get(emotion_1):
                        # round the intensity float to 2 decimal place
                        self.emotion_intensity[emotion_1] = round(intensity, 2)
                        self.wordCloudBag.append(sentence)
                        self.sentenceExamples.update([tuple((round(intensity, 2), emotion_1, sentence))])

            # process split chart values
            self.processSplitChartValues()

        except pd.errors.EmptyDataError:
            print("Nothing to classify, the file is empty")
        finally:
            print("\nThe Intensity level of each Emotion:")
            self.prettyPrint(self.emotion_intensity.items(), "percent")

            print("\nThe Amount of each Emotion:")
            self.prettyPrint(self.emotion_count.items())

            print("\nSites and associated article primary emotion_1: ")
            print(f"website: {*self.emotions,}")
            self.prettyPrint(self.emotionsPerSiteDict.items(), "lst")

            print("\nExamples of emotion_1 based sentences: ")
            sentenceExampleList = list(self.sentenceExamples)
            sentenceExampleList.sort(key=lambda tup: tup[0], reverse=True)
            for item in sentenceExampleList[0:int(len(sentenceExampleList) / 2)]:
                print(f"{item[0]:.1%} {item[1]} = {item[2]}")

    def processSplitChartValues(self):
        # total site visits = the number of sites visited
        self.total_sites = len(self.emotionsPerSiteDict)

        for _ in range(self.total_sites):
            for siteEmotionDict in self.emotionsPerSiteDict.values():
                self.splitChartValues.append(list(siteEmotionDict.values()))

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
