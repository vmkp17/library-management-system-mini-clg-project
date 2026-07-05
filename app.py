from flask import Flask, render_template, request
from database import db
from models import Book

app = Flask(__name__)

# Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


# ---------------- HOME ----------------
@app.route("/")
def home():

    total_books = Book.query.count()
    total_categories = db.session.query(Book.category).distinct().count()

    return render_template(
        "index.html",
        total_books=total_books,
        total_categories=total_categories
    )


# ---------------- CATEGORIES ----------------
@app.route("/categories")
def categories():

    category_list = [
        "Programming",
        "Artificial Intelligence",
        "Data Science",
        "Cyber Security",
        "Networking",
        "Mathematics",
        "Business",
        "History",
        "Psychology",
        "Fiction"
    ]

    return render_template(
        "categories.html",
        categories=category_list
    )


# ---------------- BOOKS ----------------
@app.route("/books/<category>")
def books(category):

    books = Book.query.filter_by(category=category).all()

    return render_template(
        "books.html",
        books=books,
        category=category
    )


# ---------------- SEARCH ----------------
@app.route("/search")
def search():

    keyword = request.args.get("keyword", "")

    books = []

    if keyword:
        books = Book.query.filter(
            (Book.book_id.contains(keyword)) |
            (Book.book_name.contains(keyword)) |
            (Book.author.contains(keyword)) |
            (Book.publisher.contains(keyword))
        ).all()

    return render_template(
        "search.html",
        books=books,
        keyword=keyword
    )


# ---------------- STATISTICS ----------------
@app.route("/stats")
def stats():

    total_books = Book.query.count()
    total_categories = db.session.query(Book.category).distinct().count()

    categories = [
        "Programming",
        "Artificial Intelligence",
        "Data Science",
        "Cyber Security",
        "Networking",
        "Mathematics",
        "Business",
        "History",
        "Psychology",
        "Fiction"
    ]

    stats_data = {}

    for category in categories:
        stats_data[category] = Book.query.filter_by(category=category).count()

    return render_template(
        "stats.html",
        total_books=total_books,
        total_categories=total_categories,
        stats_data=stats_data
    )


# ---------------- CREATE DATABASE ----------------
with app.app_context():
    db.create_all()


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(debug=True)