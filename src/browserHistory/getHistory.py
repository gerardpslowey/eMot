import sys
from pathlib import Path
from .browsers import Chrome, Firefox, Safari, Edge, Opera, Brave
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

class GetHistory():
    
    def getHistory(self, filtr, browser):
        #if blank, then use all dates
        df = '' if not filtr else self.dateFilter(filtr)

        try:
            f = globals()[browser]()                    # browser
            outputs = f.fetchHistory()
            his = outputs.histories
            urlDict = {}

            for date, url in his:
                if date > df:
                    urlDict[date] = url
            return urlDict
        except Exception as e:
            print(f"{e} : Make sure your browser choice is valid and spelled correctly.")

    def dateFilter(self, times):

        #def hour()
        if times == 'Hour':
            return self.strFormat(datetime.now() - timedelta(hours=1))

        #def day()
        elif times == 'Day':
            return self.strFormat(datetime.now() - timedelta(1))

        #def week()
        elif times == 'Week':
            return self.strFormat(datetime.now() - timedelta(days=7))

        #def month()
        elif times == 'Month':
            return self.strFormat(datetime.now() + relativedelta(months=-1))

        # def year()
        elif times == 'Year':
            return self.strFormat(datetime.now() + relativedelta(years=-1))

        else:
            raise ValueError("Make sure your filter choice is valid and spelled correctly.")

    def strFormat(self, time):
        return time.strftime("%Y-%m-%d %H:%M:%S")   #makes the date a string
