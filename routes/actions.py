from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from models import ActionModel
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
# from db import stores
from schemas import ActionsSchema, ActionsBaseSchema

blp = Blueprint("actions", __name__, description = "actions controller")

@blp.route("/actions/<int:item_id>")
class User(MethodView):
    @blp.doc(parameters=[{'name': 'item_id','in': 'path','description': 'The ID of the user','required': True,'schema': {'type': 'integer'}}])
    @blp.response(200, ActionsSchema)
    def get(self, item_id):
        item = ActionModel.query.get_or_404(item_id)
        return item
    
    @blp.doc(parameters=[{'name': 'item_id','in': 'path','description': 'The ID of the user','required': True,'schema': {'type': 'integer'}}])
    def delete(self, item_id):
        item = ActionModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"msg":"user deleted"}
    
    @blp.doc(parameters=[{'name': 'item_id','in': 'path','description': 'The ID of the user','required': True,'schema': {'type': 'integer'}}])
    @blp.arguments(ActionsBaseSchema)
    @blp.response(200, ActionsSchema)
    def put(self, item_data, item_id):
        item = ActionModel.query.get_or_404(item_id)

        item.stage = item_data['stage']
        item.kind = item_data['kind']
        item.key_number = item_data['key_number']
        item.paramaters = item_data['paramaters']
        
        db.session.add(item)
        db.session.commit()

        return item
    
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