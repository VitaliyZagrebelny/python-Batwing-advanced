import http
import os
import sys
import http
sys.path.append(os.path.abspath('..'))
from flask import Blueprint, jsonify, request
from database import db
from models.books import Book
from serializers.books import BookSchema
from marshmallow import ValidationError

book_router = Blueprint('book', __name__, url_prefix='/book')


@book_router.route('')
def get():
    book_schema = BookSchema()

    books = Book.query.order_by(Book.id)

    book_json = book_schema.dump(books, many=True)
    return jsonify(book_json)


@book_router.route('/<int:id_>')
def retrieve(id_):
    book_schema = BookSchema()
    book = Book.query.filter_by(id=id_).first()
    book_json = book_schema.dump(book)
    return jsonify(book_json)


@book_router.route('', methods=['POST'])
def create():
    data = request.get_json(force=True)

    schema = BookSchema()
    try:
        book_data = schema.load(data)
        new_book = Book(title=book_data['title'])
        db.session.add(new_book)
        db.session.commit()

        new_book_json = schema.dump(new_book)
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return new_book_json


@book_router.route('/<int:id_>', methods=['PUT'])
def update(id_):
    data = request.get_json(force=True)

    schema = BookSchema()
    try:
        book_data = schema.load(data)
        book = Book.query.filter_by(id=id_).first()
        book.title = book_data['title']
        db.session.add(book)
        db.session.commit()

        new_book_json = schema.dump(book)
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return new_book_json


@book_router.route('/<int:id_>', methods=['DELETE'])
def delete(id_):
    Book.query.filter_by(id=id_).delete()
    db.session.commit()
    return {}, http.HTTPStatus.NO_CONTENT


