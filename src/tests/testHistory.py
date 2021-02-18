import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.absolute())) 
from browserHistory.getHistory import GetHistory

def main():
    test = GetHistory()
    history = test.get_history()
    print(history)

if __name__ == "__main__":
    main()