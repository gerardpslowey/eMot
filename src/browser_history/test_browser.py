from browsers import Chrome
from browsers import Firefox
from browsers import Safari
from browsers import Edge
from browsers import Opera
from browsers import Brave

def main():
    browser = input("Enter your browser: ")
    f = globals()[browser]()
    outputs = f.fetch_history()
    his = outputs.histories

    file = open("urls.txt", "w")

    for line in his:
        #line[0] = date
        #line[1] = website
        file.write(line[1] + "\n")
    file.close()

if __name__ == "__main__":
    main()