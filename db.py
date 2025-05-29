import sqlite3

CONN = sqlite3.connect('magazine.db')
CURSOR = CONN.cursor()

def initialize_database():
    CURSOR.execute("DROP TABLE IF EXISTS articles")
    CURSOR.execute("DROP TABLE IF EXISTS authors")

    CURSOR.execute("""
        CREATE TABLE authors (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        )
    """)

    CURSOR.execute("""
        CREATE TABLE articles (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            author_id INTEGER,
            FOREIGN KEY (author_id) REFERENCES authors(id)
        )
    """)

    CONN.commit()
