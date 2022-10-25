# need to install sqlite3

import sqlite3
from lego_api import get_sets, get_themes

#print(get_sets("31062-1"))
# make database

# connect and create database
con = sqlite3.connect("lego.db")

# create cursor to execute statements
cur = con.cursor()

# make set table, set types and key
cur.execute(
"""
CREATE TABLE IF NOT EXISTS sets (
    set_num TEXT PRIMARY KEY,
    set_name TEXT NOT NULL,
    year INT NOT NULL,
    theme_id INT NOT NULL,
    num_parts INT NOT NULL
);
"""
)


# make theme table, set types and key

# load single set

# load single theme

# back up

# close connection

# proper string formatting


