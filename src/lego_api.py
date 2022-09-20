"""
Connect to rebrickable rest api and return data by set number.
"""

import os
import pandas as pd
from requests.auth import HTTPBasicAuth
import requests

from dotenv import load_dotenv

# load api key
load_dotenv()
KEY = os.getenv("REBRICKABLE_KEY", default="NO_KEY")

# update set list

# load set numbers to list from pandas
sets = pd.read_csv("./input_data/sets.csv")["set_num"].tolist()

# build request url
url = 'https://rebrickable.com/api/v3/lego/themes/'
headers = {'Authorization': "key " + KEY}
req = requests.get(url, headers=headers)
print(req.url)
print(req)

url = 'https://rebrickable.com/api/v3/lego/sets/31062-1/'
headers = {
        "Accept": "application/json",
        "Authorization": "key " + KEY
}
req = requests.get(url, headers=headers)
print(req.url)
print(req)
# start request

# return request

# parse request into df

# print head
