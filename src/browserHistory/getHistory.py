import sys
from pathlib import Path
from .browsers import Chrome, Firefox, Safari, Edge, Opera, Brave
from .dateFilter import DateFilter

class GetHistory():
    
    def get_history(self):

        print("Time filters include 'hour', 'day', 'week', 'month', or 'year' or '' (all time).")
        filtr = input('Filter the date: ')

        print("Browser options include 'Chrome', 'Firefox', 'Safari', 'Edge', 'Opera', and 'Brave'.")
        browser = input('Enter the browser: ')

        #Check if input not empty and in the possible options.
        if filtr in DateFilter.times:
            date_filter = getattr(DateFilter(), filtr)()

        #if blank, then use all dates
        elif not filtr:
            date_filter = ''
        else:
            raise ValueError("Make sure your filter choice is valid and spelled correctly.")

        try:
            f = globals()[browser]()                    # browser
            outputs = f.fetch_history()
            his = outputs.histories

            urlDict = {}

            for date, url in his:
                if date > date_filter:
                    urlDict[date] = url

            return urlDict

        except Exception as e:
            print(f"{e} : Make sure your browser choice is valid and spelled correctly.")


