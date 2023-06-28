"""
Author:
Purpose:  CRUD for mysql edition
Date："""
import argparse
from flask import  Flask,make_response,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.model import Model

import pymysql
from marshmallow_sqlalchemy import  SQLAlchemySchema as ModelSchema
from marshmallow import fields,schema,Schema

app = Flask(__name__)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://app:app123456@127.0.0.1:27001/rfb'


db = SQLAlchemy(app)


class Author(Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    specialisation = db.Column(db.String(50))


    def create(self):
        db.session.add(self)
        db.session.commit()
        return  self

    def __init__(self,name, specialisation):
        self.name = name
        self.specialisation = specialisation

    def __repr__(self):
        return '<Product %d>' % self.id

class AuthorSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    specialisation = fields.Str()



@app.route("/authors",methods=['GET'])
def get_author():
    # authros get from database
    authors = Author.query.all()
    authors = AuthorSchema(many=True).dump(authors)
    return make_response(jsonify({"authors":authors}))

@app.route("/authors/<id>",methods=['GET'])
def get_author_by_id(id):
    # id from query as arguemtn of function
    author = Author.query.get(id)
    author = AuthorSchema().dump(author)
    return make_response(jsonify({"author":author}))


@app.route("/authors/<id>",methods=['PUT'])
def update_author_by_id(id):
    # id from query as arguemtn of function

    # get parameter
    data = request.get_json()
    author = Author.query.get(id)
    #update
    if data.get("name"):
        author.name = data.get("name")
    if data.get("specialisation"):
        author.specialisation = data.get("specialisation")
    author.create()

    # get from db again
    author = Author.query.get(id)
    author = AuthorSchema().dump(author)
    return make_response(jsonify({"author":author}))

@app.route("/authors/<id>",methods=['DELETE'])
def delete_author_by_id(id):
    # id from query as arguemtn of function

    # get parameter
    author = Author.query.get(id)
    db.session.delete(author)
    db.session.commit()
    #updat
    return make_response("", 204)

@app.route("/authors",methods=['POST'])
def create_author():
    # authros get from database
    data = request.get_json()
    author = AuthorSchema().load(data)
    author = Author(author["name"],author["specialisation"])
    author.create()
    authors = AuthorSchema().dump(author)
    return make_response(jsonify({"author":authors}), 201)

def main():
    """the entrance of this file"""
    app.run(host="0.0.0.0",port=5001,debug=True)


if __name__ == '__main__':
    main()
