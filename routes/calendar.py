from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from models import CalendarModel
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
# from db import stores
from schemas import CalendarSchema, CalendarBaseSchema

blp = Blueprint("calendar", __name__, description = "calendar controller")

@blp.route("/calendar/<int:item_id>")
class User(MethodView):
    @blp.doc(parameters=[{'name': 'item_id','in': 'path','description': 'The ID of the user','required': True,'schema': {'type': 'integer'}}])
    @blp.response(200, CalendarSchema)
    def get(self, item_id):
        item = CalendarModel.query.get_or_404(item_id)
        return item
    
    @blp.doc(parameters=[{'name': 'item_id','in': 'path','description': 'The ID of the user','required': True,'schema': {'type': 'integer'}}])
    def delete(self, item_id):
        item = CalendarModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"msg":"user deleted"}
    
    @blp.doc(parameters=[{'name': 'item_id','in': 'path','description': 'The ID of the user','required': True,'schema': {'type': 'integer'}}])
    @blp.arguments(CalendarBaseSchema)
    @blp.response(200, CalendarSchema)
    def put(self, item_data, item_id):
        item = CalendarModel.query.get_or_404(item_id)

        item.taken_date = item_data['taken_date']
        item.room_number = item_data['room_number']
        

        db.session.add(item)
        db.session.commit()

        return item
    
@blp.route("/calendar")   
class Calendar(MethodView):
    @blp.response(200, CalendarSchema(many=True))
    def get(self):
        return CalendarModel.query.all()
    
    @blp.arguments(CalendarSchema)
    @blp.response(201, CalendarSchema)
    def post(self, user_data):
        store = CalendarModel(**user_data)
        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(400, message="same phone number exist")    
        except SQLAlchemyError:
            abort(500, message="an error occured while inserting calendar")

        return store       