from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from models import UserModel
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
# from db import stores
from schemas import UsersSchema, UsersBaseSchema, ItemIdSchema

blp = Blueprint("users", __name__, description = "users controller")


@blp.route("/users/<int:item_id>")
class User(MethodView):
    @blp.doc(parameters=[{'name': 'item_id','in': 'path','description': 'The ID of the user','required': True,'schema': {'type': 'integer'}}])
    @blp.response(200, UsersSchema)
    def get(self, item_id):
        item = UserModel.query.get_or_404(item_id)
        return item
    
    @blp.doc(parameters=[{'name': 'item_id','in': 'path','description': 'The ID of the user','required': True,'schema': {'type': 'integer'}}])
    def delete(self, item_id):
        item = UserModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"msg":"user deleted"}
    
    @blp.doc(parameters=[{'name': 'item_id','in': 'path','description': 'The ID of the user','required': True,'schema': {'type': 'integer'}}])
    @blp.arguments(UsersBaseSchema)
    @blp.response(200, UsersSchema)
    def put(self, item_data, item_id):
        item = UserModel.query.get_or_404(item_id)

        item.name = item_data['name']
        item.email = item_data['email']
        item.phone_number = item_data['phone_number']
        item.password = item_data['password']
        item.account = item_data['account']
        item.token = item_data['token']

        db.session.add(item)
        db.session.commit()

        return item
    
@blp.route("/users")   
class Users(MethodView):
    @blp.response(200, UsersSchema(many=True))
    def get(self):
        print("hi")
        return UserModel.query.all()
    
    @blp.arguments(UsersSchema)
    @blp.response(201, UsersSchema)
    def post(self, user_data):
        store = UserModel(**user_data)
        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(400, message="same phone number exist")    
        except SQLAlchemyError:
            abort(500, message="an error occured while inserting user")

        return store       