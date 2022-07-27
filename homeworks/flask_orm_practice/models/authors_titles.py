from database import db


class AuthorTitle(db.Model):
    __tablename__ = 'author_title'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)