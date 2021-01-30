from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

# To use dateutil install the following:
#   pip install python-dateutil

def main():
    now = datetime.now()

    print("Today's Date: ", strformat(now))
    print("Hour: ", hour(now)) 
    print("Day: ", day(now)) 
    print("Week: ", week(now)) 
    print("Month: ", month(now))
    print("Year: ", year(now))

def hour(time):
    return strformat(time - timedelta(hours=1))

def day(time):
    return strformat(time - timedelta(1))

def week(time):
    return strformat(time - timedelta(days=7))

def month(time):
    return strformat(time.replace(day=1) + relativedelta(months=+1))

def year(time):
    return strformat(time + relativedelta(years=-1))

#def allTime(time):
    # return all the dates

def strformat(time):
    return time.strftime("%Y-%m-%d %H:%M:%S")   #makes the date a string

if __name__ == '__main__':
    main()