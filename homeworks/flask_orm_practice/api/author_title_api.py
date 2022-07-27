import os
import sys

sys.path.append(os.path.abspath(".."))

import http

from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from database import db
from models.authors_titles import AuthorTitle
from models.books import Book
from models.authors import Author
from serializers.authors_titles import AuthorsTitlesSchema
from serializers.authors import AuthorSchema
from serializers.books import BookSchema
author_title_router = Blueprint("author_title", __name__, url_prefix="/author_title")

@author_title_router.route("")
def get():
    author_title_schema = AuthorsTitlesSchema()

    author_titles = AuthorTitle.query.order_by(AuthorTitle.id)
    author_titles_json = author_title_schema.dump(author_titles, many=True)
    return jsonify(author_titles_json)


@author_title_router.route("/<int:id_>")
def retrieve(id_):
    author_title_schema = AuthorsTitlesSchema()
    author_title = AuthorTitle.query.filter_by(id=id_).first()
    author_title_json = author_title_schema.dump(author_title)
    return jsonify(author_title_json)


@author_title_router.route("/<int:author_id>/<int:book_id>", methods=["POST"])
def create(author_id, book_id):
    author_schema = AuthorSchema()
    author = Author.query.filter_by(id=author_id).first()

    book_schema = BookSchema()
    book = Book.query.filter_by(id=book_id).first()

    schema = AuthorsTitlesSchema()

    if not author is None and not book is None:
        book_json = book_schema.dump(book)
        author_json = author_schema.dump(author)
        new_author_title = AuthorTitle(author=author_json["name_lastname"], title=book_json["title"])
        db.session.add(new_author_title)
        db.session.commit()

        new_author_title_json = schema.dump(new_author_title)

        return jsonify(new_author_title_json)
    elif author is None:
        return "This author does not exists"
    elif book is None:
        return "This book does not exists"


@author_title_router.route("/<int:id_>/<int:author_id>/<int:book_id>", methods=["PUT"])
def update(id_, author_id, book_id):
    author_schema = AuthorSchema()
    author = Author.query.filter_by(id=author_id).first()

    book_schema = BookSchema()
    book = Book.query.filter_by(id=book_id).first()

    schema = AuthorsTitlesSchema()
    author_title = AuthorTitle.query.filter_by(id=id_).first()

    if not author is None and not book is None:
        book_json = book_schema.dump(book)
        author_json = author_schema.dump(author)
        author_title.author = author_json["name_lastname"],
        author_title.title = book_json["title"]
        db.session.add(author_title)
        db.session.commit()

        new_author_title_json = schema.dump(author_title)

        return jsonify(new_author_title_json)
    elif author is None:
        return "This author does not exists"
    elif book is None:
        return "This book does not exists"


@author_title_router.route("/<int:id_>", methods=["DELETE"])
def delete(id_):
    author_title = AuthorTitle.query.filter_by(id=id_).first()
    if not author_title is None:
        AuthorTitle.query.filter_by(id=id_).delete()
        db.session.commit()
        return {}, http.HTTPStatus.NO_CONTENT
    else:
        return "Record doesn't exists", http.HTTPStatus.BAD_REQUEST