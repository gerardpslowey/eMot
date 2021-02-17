from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

class DateFilter:

    times = ['hour','day','week','month','year']

    def hour(self):
        return self.strformat(datetime.now() - timedelta(hours=1))

    def day(self):
        return self.strformat(datetime.now() - timedelta(1))

    def week(self):
        return self.strformat(datetime.now() - timedelta(days=7))

    def month(self):
        return self.strformat(datetime.now() + relativedelta(months=-1))

    def year(self):
        return self.strformat(datetime.now() + relativedelta(years=-1))

    def strformat(self,time):
        return time.strftime("%Y-%m-%d %H:%M:%S")   #makes the date a string