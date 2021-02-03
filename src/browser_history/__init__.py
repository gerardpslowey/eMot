from browser_history.browsers import Firefox

def get_history():
    f = Firefox()
    outputs = f.fetch_history()
    his = outputs.histories

    selected = his[:5]

    for element in selected:
        print(element, end = "\n")

    return selected