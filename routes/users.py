from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from models import UserModel
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
# from db import stores
from schemas import UsersSchema

blp = Blueprint("users", __name__, description = "users controller")


@blp.route("/users")   
class Users(MethodView):
    @blp.response(200, UsersSchema(many=True))
    def get(self):
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