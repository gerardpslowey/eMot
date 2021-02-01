import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.absolute()))

from browser_history.browsers import Firefox

def get_history():
    f = Firefox()
    outputs = f.fetch_history()
    his = outputs.histories

    selected = his[50:100]

    for element in selected:
        print(element, end = "\n")
