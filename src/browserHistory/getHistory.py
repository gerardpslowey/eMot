import sys
from pathlib import Path
from .browsers import Chrome, Firefox, Safari, Edge, Opera, Brave
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

class GetHistory():
    
    def get_history(self):

        print("Time filters include 'hour', 'day', 'week', 'month', or 'year' or '' (all time).")
        filtr = input('Filter the date: ')

        print("Browser options include 'Chrome', 'Firefox', 'Safari', 'Edge', 'Opera', and 'Brave'.")
        browser = input('Enter the browser: ')

        #if blank, then use all dates
        df = '' if not filtr else self.date_filter(filtr)

        try:
            f = globals()[browser]()                    # browser
            outputs = f.fetch_history()
            his = outputs.histories

            urlDict = {}

            for date, url in his:
                if date > df:
                    urlDict[date] = url

            return urlDict

        except Exception as e:
            print(f"{e} : Make sure your browser choice is valid and spelled correctly.")

    def date_filter(self, times):

        #def hour()
        if times == 'hour':
            return self.strformat(datetime.now() - timedelta(hours=1))

        #def day()
        elif times == 'day':
            return self.strformat(datetime.now() - timedelta(1))

        #def week()
        elif times == 'week':
            return self.strformat(datetime.now() - timedelta(days=7))

        #def month()
        elif times == 'month':
            return self.strformat(datetime.now() + relativedelta(months=-1))

        # def year()
        elif times == 'year':
            return self.strformat(datetime.now() + relativedelta(years=-1))

        else:
            raise ValueError("Make sure your filter choice is valid and spelled correctly.")

    def strformat(self, time):
        return time.strftime("%Y-%m-%d %H:%M:%S")   #makes the date a string


