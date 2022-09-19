"""
Connect to rebrickable rest api and return data by set number.
"""

import os
import pandas
import requests

# required to load in .env during python execution
from dotenv import load_dotenv

# load api key
load_dotenv()
KEY = os.getenv("REBRICKABLE_KEY", default="NO_KEY")
print(KEY)

# load set numbers to list

# build request url

# start request

# return request

# parse request into df

# print head
