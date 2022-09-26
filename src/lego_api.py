"""
Connect to rebrickable rest api and return data by set number.

API does not have parameters to embedded a set list payload into the call. 

Have to retrieve details for each set individually and use a short sleep to follow rules.
"""

import os
import json
import time
import pandas
import requests

from dotenv import load_dotenv

# load api key
load_dotenv()
KEY = os.getenv("KEY")

# load set ids
set_ids = pandas.read_csv("./input_data/sets.csv")["set_num"].tolist()

# set headers
headers = {
        "Accept": "application/json",
        "Authorization": "key " + KEY
}

# helper to get run request
def get_sets(set_id):
    url = f"https://rebrickable.com/api/v3/lego/sets/{set_id}"
    req = requests.get(url=url, headers=headers)
    time.sleep(1.1)
    return req.json()

def get_themes():
    url = "https://rebrickable.com/api/v3/lego/themes/?page=1&page_size=500"
    req = requests.get(url=url, headers=headers)
    time.sleep(1.1)
    return req.json()["results"]

# request data for each set
set_data = [get_sets(set_id) for set_id in set_ids]
print(set_data)

# load to df
set_df = pandas.DataFrame(set_data)

# print head
print(set_df.head())

# count sets and sum parts
print(set_df["num_parts"].sum())
print(set_df["num_parts"].count())

# request themes
themes_data = pandas.DataFrame(get_themes())
themes_data
print(themes_data)

# join sets to themes and save
join_data = set_df.merge(themes_data, left_on="theme_id", right_on="id", validate="m:1")
join_data.to_csv("output_data/join_data.csv")
print(join_data.head())
print(join_data["name_y"].value_counts())

