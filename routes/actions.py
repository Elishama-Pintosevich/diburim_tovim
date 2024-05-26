from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from models import ActionModel
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
# from db import stores
from schemas import ActionsSchema

blp = Blueprint("actions", __name__, description = "actions controller")

@blp.route("/actions")   
class Actions(MethodView):
    @blp.response(200, ActionsSchema(many=True))
    def get(self):
        return ActionModel.query.all()
    
    @blp.arguments(ActionsSchema)
    @blp.response(201, ActionsSchema)
    def post(self, user_data):
        store = ActionModel(**user_data)
        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(400, message="same phone number exist")    
        except SQLAlchemyError:
            abort(500, message="an error occured while inserting action")

        return store       