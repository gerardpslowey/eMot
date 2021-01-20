from browser_history.browsers import Chrome

def main():
    f = Chrome()
    outputs = f.fetch_history()
    his = outputs.histories

    for line in his:
        print(line, end="\n")

if __name__ == "__main__":
    main()