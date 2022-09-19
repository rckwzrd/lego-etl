"""
Connect to rebrickable api and return information by set number.
"""

import rebrick
import pandas as pd

api_key = "GET FROM REBRICKABLE"
user_token = "GET FROM REBRICKABLE"

# init rebrick api
rb = rebrick.Rebrick(api_key, user_token, silent=True)

# load set nums to list 
my_sets = pd.read_csv("C:/Users/mrhoa/projects/lego/input_data/my_sets.csv", usecols=[0])
my_sets_list = list(my_sets["set_num"].astype("str").values)

# query for specific set by num
data = rb.get_set("79115")
print(data)

# get set info for all set nums
for sets in my_sets_list:
    data = rb.get_set(sets)
    print(sets)
    print(data)
    print("****")

# if user token is not provided on init you can get it later to access user data
# rb.login("your_username_here", "your_password_here")

# get user partlists
# data = rb.get_users_partlists()
# print(data)