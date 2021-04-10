from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from .browsers import Chrome, Firefox, Safari, Edge, Opera, Brave  # noqa


class GetHistory():

    def getHistory(self, filtr, browser):
        # if blank, then use all dates
        df = '' if not filtr else self.dateFilter(filtr)
        browser = browser.capitalize()

        try:
            # f will be one of the imported Browsers
            f = globals()[browser]()
            outputs = f.fetchHistory()
            his = outputs.histories
            urlDict = {}

            for date, url in his:
                if date > df:
                    urlDict[date] = url
            return urlDict
        except Exception as e:
            raise SystemExit(f"{e} : Make sure your BROWSER choice is valid and spelled correctly.")

    def dateFilter(self, times):

        # def hour()
        if times == 'Hour':
            return self.strFormat(datetime.now() - timedelta(hours=1))

        # def day()
        elif times == 'Day':
            return self.strFormat(datetime.now() - timedelta(1))

        # def week()
        elif times == 'Week':
            return self.strFormat(datetime.now() - timedelta(days=7))

        # def month()
        elif times == 'Month':
            return self.strFormat(datetime.now() + relativedelta(months=-1))

        # def year()
        elif times == 'Year':
            return self.strFormat(datetime.now() + relativedelta(years=-1))

        elif times == 'All':
            return ''

        else:
            raise ValueError("Make sure your FILTER choice is valid and spelled correctly.")

    def strFormat(self, time):

        # makes the date a string
        return time.strftime("%Y-%m-%d %H:%M:%S")
