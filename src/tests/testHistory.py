import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.absolute())) 
from browserHistory.getHistory import GetHistory

def main():

    print("Time filters include 'hour', 'day', 'week', 'month', or 'year' or '' (all time).")
    filtr = input('Filter the date: ')
    print("Browser options include 'Chrome', 'Firefox', 'Safari', 'Edge', 'Opera', and 'Brave'.")
    browser = input('Enter the browser: ')
    test = GetHistory()
    history = test.get_history(filtr, browser)
    print(history)

if __name__ == "__main__":
    main()