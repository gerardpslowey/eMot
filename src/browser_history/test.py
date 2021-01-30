import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.absolute()))

from browser_history.browsers import Chrome, Firefox, Safari, Edge, Opera, Brave

def main():
    browser = input('Enter the browser: ')
    f = globals()[browser]()
    outputs = f.fetch_history()
    his = outputs.histories

    selected = his[:50]

    for element in selected:
        print(element, end = "\n")

if __name__ == "__main__":
    main()
