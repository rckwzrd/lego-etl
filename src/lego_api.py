"""
Connect to rebrickable rest api and return data by set number.

API does not have parameters to embedded a set list payload into the call. 

Have to retrieve details for each set individually and use a short sleep to follow rules.

There may be a way to filter on a list of sets.
"""

import os
import json
import pandas as pd
import requests

from dotenv import load_dotenv

# load api key
load_dotenv()
KEY = os.getenv("REBRICKABLE_KEY")

# load set ids and build list of urls
set_ids = pd.read_csv("./input_data/sets.csv")["set_num"].tolist()
base_url = 'https://rebrickable.com/api/v3/lego/sets/'
set_urls = [base_url+ids for ids in set_ids]
 
# build request
for url in set_urls:
    # make request
    # extract data
    # sleep 1.1sec
    pass

headers = {
        "Accept": "application/json",
        "Authorization": "key " + KEY
}
req = requests.get(url="https://rebrickable.com/api/v3/lego/sets/60181-1", headers=headers)
print(req.url)
print(type(req.json()))
print(req.ok)
print(req.status_code)



# request themes
url = 'https://rebrickable.com/api/v3/lego/themes/'
headers = {'Authorization': "key " + KEY}
req = requests.get(url, headers=headers)
