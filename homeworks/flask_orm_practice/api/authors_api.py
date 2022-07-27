import os
import sys

sys.path.append(os.path.abspath('..'))
import http
import os
import sys
from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

sys.path.append(os.path.abspath('..'))
from database import db
from models.authors import Author
from serializers.authors import AuthorSchema

author_router = Blueprint('author', __name__, url_prefix='/author')


@author_router.route('')
def get():
    author_schema = AuthorSchema()

    authors = Author.query.order_by(Author.email)
    authors_json = author_schema.dump(authors, many=True)
    return jsonify(authors_json)


@author_router.route('/<int:id_>')
def retrieve(id_):
    author_schema = AuthorSchema()
    author = Author.query.filter_by(id=id_).first()
    author_json = author_schema.dump(author)
    return jsonify(author_json)


@author_router.route('', methods=['POST'])
def create():
    data = request.get_json(force=True)

    schema = AuthorSchema()
    try:
        author_data = schema.load(data)
        new_author = Author(name_lastname=author_data['name_lastname'])
        db.session.add(new_author)
        db.session.commit()

        new_author_json = schema.dump(new_author)
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return new_author_json


@author_router.route('/<int:id_>', methods=['PUT'])
def update(id_):
    data = request.get_json(force=True)

    schema = AuthorSchema()
    try:
        author_data = schema.load(data)
        author = Author.query.filter_by(id=id_).first()
        author.name_lastname = author_data['name_lastname']
        db.session.add(author)
        db.session.commit()

        new_author_json = schema.dump(author)
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return new_author_json


@author_router.route('/<int:id_>', methods=['DELETE'])
def delete(id_):
    Author.query.filter_by(id=id_).delete()
    db.session.commit()
    return {}, http.HTTPStatus.NO_CONTENT

# @author_router.route('/<int:id_>/add_group/<int:group_id>', methods=['POST'])
# def add_to_group(id_, group_id):
#     user = User.query.filter_by(id=id_).first()
#     if group := Group.query.filter_by(id=group_id).first():
#         user.group_id = group.id
#         db.session.add(user)
#         db.session.commit()
#         schema = UserSchema()
#         new_user_json = schema.dump(user)
#         return new_user_json, http.HTTPStatus.OK
#     else:
#         return {"No group found"}, http.HTTPStatus.BAD_REQUEST
