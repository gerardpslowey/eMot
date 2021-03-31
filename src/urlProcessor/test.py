import json

with open("Blacklists.json") as json_file:
    data = json.load(json_file)
    # for p in data['Blacklists']:
    #         for url in p['urlSets']:
    #             print(url)


    data['Blacklists']['urlSets'].append("www.gmail.com")