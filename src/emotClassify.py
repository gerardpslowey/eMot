import pandas as pd
import pickle
import threading
from utils.urlFilter import base
import copy
from collections import OrderedDict
from utils.urlFilter import base

scrapedFile = 'sentimentAnalysis/scraped.csv'


class EmotClassify:
    def __init__(self):
        self.emotions = ['anger', 'fear', 'joy', 'surprise', 'happiness', 'sadness']
        # make a nested dictionary setting the emotion count values to zero
        self.emotions_dict = dict.fromkeys(self.emotions, 0)

        self.emotion_count = {
            "anger": 0,
            "fear": 0,
            "joy": 0,
            "surprise": 0,
            "happiness": 0,
            "sadness": 0
        }

        self.emotion_intensity = {
            "anger": 0,
            "fear": 0,
            "joy": 0,
            "surprise": 0,
            "happiness": 0,
            "sadness": 0
        }

        self.emotionsPerSiteDict = {}
        # self.emotionsPerSiteDict = OrderedDict()

        self.site_visit_counts = None
        self.total_sites = 0

        self.svc_model = "models/svc.pkl"
        self.svc_tfidf_file = "models/svc_tfidf.pkl"
        self.model = self.loadFiles(self.svc_model)
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
        for key, value in self.site_visit_counts.items():
            print(f"{key}: {value}")

    def sentenceClassify(self):
        scraped_df = pd.read_csv(scrapedFile).astype('U')

        scraped_df['base'] = scraped_df['url'].apply(base)
        # create a list of unique base sites
        sitesList = scraped_df['base'].unique().tolist()
        # create a nested dictionary for each site
        for site in sitesList:
            self.emotionsPerSiteDict[site] = copy.deepcopy(self.emotions_dict)

        try:
            for row in scraped_df.itertuples(index=False):
                text = row[1]
                url = row[2]

                # score each sentence
                for sentence in text.split("|"):
                    sentiment_score = self.model.predict_proba(self.tfidf.transform([sentence]))
                    sentiment_name = self.model.predict(self.tfidf.transform([sentence]))

                    emotion = sentiment_name[0]
                    intensity = sentiment_score.max()

                    # count total emotion count
                    self.emotion_count[emotion] += 1
                    # count of distribution of emotions per site
                    self.emotionsPerSiteDict[url][emotion] += 1

                    if intensity > self.emotion_intensity.get(emotion):
                        # round the intensity float to 2 decimal place
                        self.emotion_intensity[emotion] = round(intensity, 2)

            # total site visits = the number of sites visited
            self.total_sites = len(self.emotionsPerSiteDict)

            for _ in range(self.total_sites):
                for siteEmotionDict in self.emotionsPerSiteDict.values():
                    self.splitChartValues.append(list(siteEmotionDict.values()))

        except pd.errors.EmptyDataError:
            print("Nothing to classify, the file is empty")
        finally:
            print("\nThe Intensity level of each Emotion:")
            for key, value in self.emotion_intensity.items():
                print(f"{key}: {value:.1%}")

            print("\nThe Amount of each Emotion:")
            for key, value in self.emotion_count.items():
                print(f"{key}: {value}")

            print("\nSites and associated article primary emotion: ")
            for key, value in self.emotionsPerSiteDict.items():
                print(f"{key}: {value}")

    # def documentClassify(self):
    #     scraped_document_df = pd.read_csv(scrapedFile).astype('U')

    #     model = self.loadFiles(self.svc_model)
    #     tfidf = self.loadFiles(self.svc_tfidf_file)

    #     scraped_document_df['base'] = scraped_document_df['url'].apply(base)
    #     # create a list of unique base sites
    #     sitesList = scraped_document_df['base'].unique().tolist()
    #     # create a nested dictionary for each site
    #     # TODO do a write up on this shallow vs deepcopies
    #     for site in sitesList:
    #         self.emotionsPerSiteDict[site] = copy.deepcopy(self.emotions_dict)

    #     try:
    #         for row in scraped_document_df.itertuples(index=False):
    #             text = row[1]
    #             url = row[2]

    #             # classify on document level
    #             sentiment_name = model.predict(tfidf.transform([text]))
    #             emotion = sentiment_name[0]
    #             # store the emotion result
    #             self.emotionsPerSiteDict[url][emotion] += 1
                        
    #         # total site visits = the number of sites visited
    #         self.total_sites = len(self.emotionsPerSiteDict)

    #         # rearranging the list of emotions 90* for the split bar chart.
    #         for _ in range(self.total_sites):
    #             for siteEmotionDict in self.emotionsPerSiteDict.values():
    #                 self.splitChartValues.append(list(siteEmotionDict.values()))

    #     except pd.errors.EmptyDataError:
    #         print("Nothing to classify, the file is empty")
    #     finally:
    #         print("\nSites and associated article primary emotion: ")
    #         for key, value in self.emotionsPerSiteDict.items():
    #             print(f"{key}: {value}")

    def negAndPos(self):
        coef_avg = 0
        for i in self.model.calibrated_classifiers_:
            coef_avg = coef_avg + i.base_estimator.coef_
        coef_avg = coef_avg / len(self.model.calibrated_classifiers_)
        # print(coef_avg)

        feature_to_coef = {
            word: coef for word, coef in zip(self.tfidf.get_feature_names(), coef_avg[0])}

        # print('Angry Words')
        for most_angry in sorted(feature_to_coef.items(), key=lambda x: x[1], reverse=True)[:25]:
            # print(most_angry)
            self.wordCloudBag.append(most_angry[0])

        # print('Sad Words')
        for most_sad in sorted(feature_to_coef.items(), key=lambda x: x[1])[:10]:
            # print(most_sad)
            self.wordCloudBag.append(most_sad[0])


    def loadFiles(self, filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)

    def get_emotions(self):
        return self.emotions

    def get_emotion_count(self):
        return self.emotion_count

    def get_emotion_intensity(self):
        return self.emotion_intensity

    def get_emotions_per_site(self):
        return self.emotionsPerSiteDict

    def get_site_count(self):
        return self.site_visit_counts

    def get_total_sites(self):
        return self.total_sites

    def get_total_site_visit(self):
        return f"{len(self.site_visit_counts)} Sites"

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

        # process3 = threading.Thread(target=self.documentClassify)
        # process3.start()
        # threads.append(process3)

        process4 = threading.Thread(target=self.negAndPos)
        process4.start()
        threads.append(process4)

        for process in threads:
            process.join()


def main():
    test = EmotClassify()
    test.startAll()

    print(test.get_wordcloud_bag())


if __name__ == '__main__':
    main()
