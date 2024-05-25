from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from models import CalendarModel
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
# from db import stores
from schemas import CalendarSchema

blp = Blueprint("calendar", __name__, description = "calendar controller")


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