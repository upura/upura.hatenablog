# -*- coding: utf-8 -*-
import requests
import json
import csv
from tqdm import tqdm

final_output = []
targetInfo = ["news",
              "published",
              "title",
              "link",
              "image",
              "pickCount",
              "publisher",
              "type"]

def makeHeader():
    header = []
    for ti in targetInfo:
        header.append(ti)
    final_output.append(header)

def getJsonInfo(url):
    json_str = requests.get(url).text
    return json.loads(json_str)

def addJsonInfo(json_dict):
    tmp_info = []
    for ti in targetInfo:
        tmp_info.append(json_dict[ti])
    final_output.append(tmp_info)

makeHeader()
# range(80001, 2557400)
for newsIndex in tqdm(range(2547000, 2557400)):
    try:
        json_dict = getJsonInfo('https://contents.newspicks.com/news/'
                                + str(newsIndex))
        addJsonInfo(json_dict)
    except:
        pass
    
with open('newspickInfo' + str(newsIndex) + '.csv', 'w', encoding='utf-8-sig') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerows(final_output)
