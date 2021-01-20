from browser_history.browsers import Firefox

def main():
    f = Firefox()
    outputs = f.fetch_history()
    his = outputs.histories

    for line in his:
        print(line, end="\n")

if __name__ == "__main__":
    main()