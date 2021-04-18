import os
import json

with open(os.getcwd() + "/stats.json", 'r') as data:
    datastore = json.load(data)

print(datastore["data"]["materials"]["coins"])