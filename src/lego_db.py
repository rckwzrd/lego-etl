import sqlite3

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


def main():
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
    main()








