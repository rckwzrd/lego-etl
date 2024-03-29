import sqlite3
from lego_api import get_themes

def connect_db(db_file):
    try:
        conn = sqlite3.connect(db_file)
        print("Connection Created")
    except sqlite3.Error as e:
        raise e
    return conn


def close_db(conn):
    try:
        conn.close()
        print("Connection Closed")
    except sqlite3.Error as e:
        raise e


def create_table(conn, table_sql):
    try:
        c = conn.cursor()
        c.execute(table_sql)
        print("Table Created")
    except sqlite3.Error as e:
        raise e


def load_table(conn, load_sql, data):
    try:
        #NOTE: context manager
        with conn:
            conn.executemany(load_sql, data)
            print("Table Hydrated")
    except sqlite3.Error as e:
        raise e


def load_theme_table():
    db_file = "lego.db"

    #NOTE: comprehension to unpack theme data
    themes = [(i["id"], i["name"]) for i in get_themes()]

    print(type(themes))
    print(type(themes[0]))
    print(themes[0])
    print(themes[1])

    #NOTE: sql insert statement, placeholders
    load_sql = """
        INSERT INTO themes VALUES(?, ?)
    """

    #NOTE: procedure
    conn = connect_db(db_file)
    load_table(conn, load_sql, themes)
    close_db(conn)


def init_lego_db():
    db_file = "lego.db"

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

    conn = connect_db(db_file)
    create_table(conn, create_themes_sql)
    create_table(conn, create_sets_sql)
    close_db(conn)


if __name__ == "__main__":
    #init_lego_db()
    load_theme_table()








