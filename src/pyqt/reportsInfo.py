from PyQt5 import QtCore, QtGui, QtWidgets
# flake8: noqa

def setStats(self):
    self.emotClassify.get_largest_emotion()
    self.emotClassify.get_sentence_intensity("joy")
    self.emotClassify.get_anger_total()
    self.emotClassify.get_sentence_intensity("fear")
    self.getFilter()
    self.getNumSites()

    emotionsDict = self.emotClassify.get_emotion_count()
    emotions = dict(sorted(emotionsDict.items(), key=lambda item: item[1], reverse= True))
    
    series = QtChart.QPieSeries()
    for emotion in emotions:
        series.append(emotion, emotionsDict[emotion])

def printTextInfo(self):
    print(self.emotion_count)
    self.largest_emotion = [key for key in self.emotion_count.keys() if self.emotion_count[key] == max(self.emotion_count.values())]
    print(f"\nThe most prominent emotion that you read was {self.largest_emotion[0]}.")
    print(contentMessage(self))

def contentMessage(self):
    if self.largest_emotion[0] == 'joy':
        return "This is great! You are looking at happy content on the web."
    elif self.largest_emotion[0] == 'sadness':
        return "Oh no! You are looking at content that is primarily sad. Try to stay away from websites that have negative content."
    elif self.largest_emotion[0] == 'anger':
        return "You are consuming content that can invoke anger. We recommend that you try to avoid this sort of content."
    elif self.largest_emotion[0] == 'fear':
        return "You are reading fear based content. Oh no! You should try to avoid this sort of content."
    else:
        return "This is good. You aren't viewing content that is very emotional."
