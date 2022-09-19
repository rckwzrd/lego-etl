"""
Merge local lego set list to data retrieved from rebrickable.

Save merged lego set list to directory.

With merged data, count total sets and bricks.
"""

import pandas as pd

# load and process rebrickable data
rb_sets = pd.read_csv("C:/Users/mrhoa/projects/lego/input_data/rebrickable_sets.csv")

# extract list of values from my sets
my_sets = pd.read_csv("C:/Users/mrhoa/projects/lego/input_data/my_sets.csv")
my_sets_list = list(my_sets["set_num"].values)

set_filter = rb_sets["set_num"].isin(my_sets_list)
rb_sets = rb_sets[set_filter]

# merge my sets and rebrickable sets
merged_sets = my_sets.merge(rb_sets,how='left',left_on="set_num",right_on='set_num')
merged_sets.to_csv("C:/Users/mrhoa/projects/lego/output_data/merged_sets.csv", index=False)

# count sets and bricks
total_sets = merged_sets["count"].sum()
total_bricks = merged_sets["num_parts"].sum()

print(f"Total number of lego sets: {total_sets}")
print(f"Total number of lego bricks: {total_bricks}")

