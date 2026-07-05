from app import app
from database import db
from models import Book

with app.app_context():

    # Delete old data (if any)
    db.session.query(Book).delete()

    categories = {
        "Programming": [
            "Python Basics", "Advanced Python", "C Programming", "C++ Fundamentals",
            "Java Programming", "JavaScript Guide", "HTML & CSS", "Data Structures",
            "Algorithms", "Web Development"
        ],
        "Artificial Intelligence": [
            "AI Basics", "Machine Learning", "Deep Learning", "Neural Networks",
            "Computer Vision", "Natural Language Processing", "Generative AI",
            "AI Ethics", "Reinforcement Learning", "AI Projects"
        ],
        "Data Science": [
            "Data Analysis", "Pandas Guide", "NumPy Essentials", "Statistics",
            "Data Visualization", "Big Data", "Data Mining", "SQL Basics",
            "Excel for Data Science", "Business Analytics"
        ],
        "Cyber Security": [
            "Ethical Hacking", "Network Security", "Cryptography", "Cyber Laws",
            "Linux Security", "Penetration Testing", "Malware Analysis",
            "Digital Forensics", "Security Tools", "Cloud Security"
        ],
        "Networking": [
            "Computer Networks", "CCNA Guide", "Routing", "Switching",
            "TCP/IP", "Wireless Networks", "Network Troubleshooting",
            "Network Design", "Firewalls", "Cloud Networking"
        ],
        "Mathematics": [
            "Calculus", "Linear Algebra", "Discrete Mathematics",
            "Probability", "Statistics", "Trigonometry", "Geometry",
            "Number Theory", "Matrices", "Graph Theory"
        ],
        "Business": [
            "Business Management", "Marketing", "Finance", "Entrepreneurship",
            "Leadership", "Accounting", "Economics", "Operations",
            "Human Resources", "Business Communication"
        ],
        "History": [
            "World History", "Indian History", "Ancient Civilizations",
            "Modern History", "Medieval History", "World Wars",
            "Freedom Movement", "Historical Leaders", "Archaeology",
            "Cultural Heritage"
        ],
        "Psychology": [
            "Introduction to Psychology", "Human Behavior", "Cognitive Psychology",
            "Social Psychology", "Personality Development", "Mental Health",
            "Emotional Intelligence", "Child Psychology", "Positive Psychology",
            "Counselling Basics"
        ],
        "Fiction": [
            "The Lost City", "Silent River", "Hidden Truth", "Dark Forest",
            "Golden Kingdom", "Last Journey", "Broken Dreams", "Magic World",
            "The Mystery House", "Final Chapter"
        ]
    }

    count = 1

    for category, books in categories.items():

        for book in books:

            new_book = Book(
                book_id=f"BK{count:03}",
                book_name=book,
                author=f"Author {count}",
                publisher=f"Publisher {count}",
                category=category
            )

            db.session.add(new_book)
            count += 1

    db.session.commit()

    print("=" * 50)
    print("✅ 100 Books Added Successfully!")
    print("=" * 50)