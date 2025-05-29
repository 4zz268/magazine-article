from db import CURSOR, CONN

class Article:
    def __init__(self, title, content, author_id, id=None):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str) and value.strip():
            self._title = value.strip()
        else:
            raise ValueError("Article title must be a non-empty string.")

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if isinstance(value, str) and value.strip():
            self._content = value.strip()
        else:
            raise ValueError("Article content must be a non-empty string.")

    @classmethod
    def create(cls, title, content, author_id):
        article = cls(title, content, author_id)
        CURSOR.execute(
            "INSERT INTO articles (title, content, author_id) VALUES (?, ?, ?)",
            (article.title, article.content, article.author_id)
        )
        CONN.commit()
        article.id = CURSOR.lastrowid
        return article

    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM articles")
        return [cls(row[1], row[2], row[3], row[0]) for row in CURSOR.fetchall()]

    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("SELECT * FROM articles WHERE id = ?", (id,))
        row = CURSOR.fetchone()
        return cls(row[1], row[2], row[3], row[0]) if row else None

    @classmethod
    def find_by_author_id(cls, author_id):
        CURSOR.execute("SELECT * FROM articles WHERE author_id = ?", (author_id,))
        return [cls(row[1], row[2], row[3], row[0]) for row in CURSOR.fetchall()]

    def delete(self):
        CURSOR.execute("DELETE FROM articles WHERE id = ?", (self.id,))
        CONN.commit()
