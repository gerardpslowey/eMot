from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from .browsers import Chrome, Firefox, Safari, Edge, Opera, Brave  # noqa


class GetHistory():
    def getHistory(self, filtr, browser):
        # if blank, then use all dates
        self.urlDict = {}

        df = '' if not filtr else self.dateFilter(filtr)
        if df is None:
            return self.urlDict

        browser = browser.capitalize()

        try:
            # f will be one of the imported Browsers
            f = globals()[browser]()
            outputs = f.fetchHistory()
            his = outputs.histories

            for date, url in his:
                if date > df:
                    self.urlDict[date] = url
        except KeyError:
            print(f"Browser spelling error: is {browser} valid?")
        except AttributeError:
            print(f"Platform error: is {browser} compatible with this machine?")
        return self.urlDict

    def dateFilter(self, times):
        # history items from the past hour
        if times == 'Hour':
            return self.strFormat(datetime.now() - timedelta(hours=1))

        # history items from the past day
        elif times == 'Day':
            return self.strFormat(datetime.now() - timedelta(1))

        # history items from the past hour
        elif times == 'Week':
            return self.strFormat(datetime.now() - timedelta(days=7))

        # history items from the past month
        elif times == 'Month':
            return self.strFormat(datetime.now() + relativedelta(months=-1))

        # history items from the past year
        elif times == 'Year':
            return self.strFormat(datetime.now() + relativedelta(years=-1))

        elif times == 'All':
            return ''

        else:
            print(f"Filter spelling error: is {times} valid?")
            return None

    def strFormat(self, time):
        # format the date as a string
        return time.strftime("%Y-%m-%d %H:%M:%S")
