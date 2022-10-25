# need to install sqlite3

import sqlite3
from lego_api import get_sets, get_themes

#print(get_sets("31062-1"))
# make database

# connect and create database

# create cursor to execute statements

# make set table, set types and key

# make theme table, set types and key

# load single set

# load single theme

# back up

# close connection

# proper string formatting

def connect_db(db_file):
    try:
        conn = sqlite3.connect(db_file)
        print("Connection Created")
    except sqlite3.Error as e:
        raise e
    return conn


def create_table(conn, table_sql):
    try:
        c = conn.cursor()
        c.execute(table_sql)
        print("Table Created")
    except sqlite3.Error as e:
        raise e


def main():
    db_file = "lego.db"
    conn = connect_db(db_file)

    create_themes_sql = """
        CREATE TABLE IF NOT EXISTS themes (
            theme_id INT PRIMARY KEY,
            theme_name TEXT NOT NULL
        );
        """

    create_sets_sql = """
        CREATE TABLE IF NOT EXISTS sets (
            set_num TEXT PRIMARY KEY,
            set_name TEXT NOT NULL,
            set_year INT NOT NULL,
            theme_id INT NOT NULL,
            num_parts INT NOT NULL,
            FOREIGN KEY (theme_id) REFERENCES themes (theme_id)
        );
        """
    create_table(conn, create_themes_sql)
    create_table(conn, create_sets_sql)


if __name__ == "__main__":
    main()








