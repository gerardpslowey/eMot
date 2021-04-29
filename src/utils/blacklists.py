import json


class Blacklists:
    """Deleter/ Adder class for JSON blacklist."""

    def __init__(self):
        self.filename = "utils/blacklists.json"

    def getItems(self, blacklist=None):
        try:
            with open(self.filename) as json_file:
                data = json.load(json_file)
                if blacklist is not None:
                    return data[blacklist]
                else:
                    return data
        except OSError:
            print(f"Could not read file {self.filename}")
            return None

    def addItem(self, item, blacklist):
        data = self.getItems()

        # blacklist is either urlSet or tagSet
        if item not in data[blacklist]:
            data[blacklist].append(item)
            self.dumpItems(data)

    def removeItem(self, item, blacklist):
        data = self.getItems()
        try:
            data[blacklist].remove(item)
            self.dumpItems(data)
        except ValueError:
            print(f"{item} not in {blacklist}")

    def dumpItems(self, data):
        with open(self.filename, "w") as json_file:
            json.dump(data, json_file, indent=4, sort_keys=True)
