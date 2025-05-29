from db import CURSOR, CONN

class Author:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and value.strip():
            self._name = value.strip()
        else:
            raise ValueError("Author name must be a non-empty string.")

    @classmethod
    def create(cls, name):
        author = cls(name)
        CURSOR.execute("INSERT INTO authors (name) VALUES (?)", (author.name,))
        CONN.commit()
        author.id = CURSOR.lastrowid
        return author

    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM authors")
        return [cls(row[1], row[0]) for row in CURSOR.fetchall()]

    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM authors WHERE id = ?", (id,))
        row = CURSOR.fetchone()
        return cls(row[1], row[0]) if row else None

    def delete(self):
        CURSOR.execute("DELETE FROM authors WHERE id = ?", (self.id,))
        CONN.commit()

    def get_articles(self):
        from models.article import Article
        return Article.find_by_author_id(self.id)
