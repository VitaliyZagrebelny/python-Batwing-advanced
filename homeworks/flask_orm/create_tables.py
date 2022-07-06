from main import db
from models.user import User
from models.lib import Book

if __name__ == '__main__':
    db.create_all()
    db.session.commit()
    db.session.add(Book(book_name="Programing"))
    db.session.commit()
    print("created tables")
