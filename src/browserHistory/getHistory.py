from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta

from .browsers import Brave, Chrome, Edge, Firefox, Opera, Safari  # noqa


class GetHistory:
    """uses the parameters filtr and browser to get the urls from the browsers."""

    def getHistory(self, filtr, browser):
        # if blank, then use all dates
        self.urlDict = {}

        dateParam = "" if not filtr else self.dateFilter(filtr)
        if dateParam is None:
            return self.urlDict

        browser = browser.capitalize()

        try:
            # one of the imported Browsers
            browserClass = globals()[browser]()
            outputs = browserClass.fetchHistory()
            his = outputs.histories

            for date, url in his:
                if date > dateParam:
                    self.urlDict[date] = url
        except KeyError:
            print(f"Browser spelling error: is {browser} valid?")
        except AttributeError:
            print(
                f"Platform error: is {browser} compatible with this machine?")
        return self.urlDict

    def dateFilter(self, times):
        # history items from the past hour
        if times == "Hour":
            return self.strFormat(datetime.now() - timedelta(hours=1))

        # history items from the past day
        elif times == "Day":
            return self.strFormat(datetime.now() - timedelta(1))

        # history items from the past hour
        elif times == "Week":
            return self.strFormat(datetime.now() - timedelta(days=7))

        # history items from the past month
        elif times == "Month":
            return self.strFormat(datetime.now() + relativedelta(months=-1))

        # history items from the past year
        elif times == "Year":
            return self.strFormat(datetime.now() + relativedelta(years=-1))

        elif times == "All":
            return ""

        else:
            print(f"Filter error: is {times} valid?")
            return None

    def strFormat(self, time):
        # format the date as a string
        return time.strftime("%Y-%m-%d %H:%M:%S")
