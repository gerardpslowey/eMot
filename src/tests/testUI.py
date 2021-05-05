import sys
from pathlib import Path
from random import SystemRandom

from PyQt5 import QtCore, QtWidgets
from wordcloud import STOPWORDS, WordCloud

from emotClassify import EmotClassify
from pyqt import main_window, metrics
from qtWorker import Worker

safe_random = SystemRandom()


sys.path.append(str(Path(__file__).parent.parent.absolute()))

stop_words = ["s", "m", "na", "co"] + list(STOPWORDS)


class Main(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    """Main GUI application. Uses eMot for scraping and emotClassify for metrics."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.showMinimized()

        self.threadpool = QtCore.QThreadPool()
        self.MetricsDashboard = metrics.MetricsDashboard("test", "test")

        self.emotClassify = EmotClassify("src")
        worker = Worker(self.emotClassify.startAll)
        self.threadpool.start(worker)
        worker.signals.finished.connect(self.enableResultsButton)
        self.MetricsDashboard.show()

    def enableResultsButton(self):
        self.startDrawing()
        self.linkNegandPosSites()
        self.displaySentences()
        self.MetricsDashboard.makeCharts(self.emotClassify)
        self.MetricsDashboard.showMaximized()

    def linkNegandPosSites(self):
        negSite, posSite = self.emotClassify.getMostPosandNeg()
        negativeSite = f"<a href=\"{negSite}\">Click here</a>"
        positiveSite = f"<a href=\"{posSite}\">Click here</a>"
        self.MetricsDashboard.negSiteEdit.setText(negativeSite)
        self.MetricsDashboard.posSiteEdit.setText(positiveSite)

    def displaySentences(self):
        negativeList, positiveList = self.emotClassify.getSentenceExamples()
        self.MetricsDashboard.displaySentenceExamples(negativeList, "negative")
        self.MetricsDashboard.displaySentenceExamples(positiveList, "positive")

    def startDrawing(self):
        negativeList, positiveList = self.emotClassify.getWordcloudBag()
        negColour, posColour = "#fcebcf", "#e6faff"
        worker = Worker(
            self.createWordcloud(negativeList, "negative", negColour)
        )  # light orange
        self.threadpool.start(worker)
        worker2 = Worker(
            self.createWordcloud(positiveList, "positive", posColour)
        )  # light blue
        self.threadpool.start(worker2)

    def createWordcloud(self, data, prefix, colour):
        if data:
            words = " ".join(data)
            wordcloud = WordCloud(
                background_color=colour, stopwords=stop_words,
                width=600, height=520
            ).generate(words)

            posNeg = prefix + "Colour"
            wordColour = getattr(self, posNeg)
            wordcloud.recolor(color_func=wordColour)

            wordCloudImage = f"pyqt/resources/{prefix}Wordcloud.png"
            wordcloud.to_file(wordCloudImage)
            self.MetricsDashboard.showImage(wordCloudImage, prefix)
        else:
            errorImage = "pyqt/resources/error.png"
            self.MetricsDashboard.showImage(errorImage, prefix)

    def negativeColour(self, word, font_size, position,  # noqa
                       orientation, random_state=3, **kwargs):  # noqa
        return "hsl(%d, 90%%, 40%%)" % safe_random.randint(250, 360)

    def positiveColour(self, word, font_size, position,  # noqa
                       orientation, random_state=3, **kwargs):  # noqa
        return "hsl(%d, 90%%, 40%%)" % safe_random.randint(90, 180)

    def closeEvent(self, event):
        """Shuts down application on close."""
        super().closeEvent(event)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    app.exec_()
