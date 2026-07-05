from database import db


class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)

    book_id = db.Column(db.String(20), unique=True, nullable=False)

    book_name = db.Column(db.String(200), nullable=False)

    author = db.Column(db.String(100), nullable=False)

    publisher = db.Column(db.String(100), nullable=False)

    category = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Book {self.book_name}>"