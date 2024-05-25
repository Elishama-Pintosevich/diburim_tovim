from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from models import BpnModel
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
# from db import stores
from schemas import BpnSchema

blp = Blueprint("bpn", __name__, description = "bpn controller")


@blp.route("/bpn")   
class Bpn(MethodView):
    @blp.response(200, BpnSchema(many=True))
    def get(self):
        return BpnModel.query.all()
    
    @blp.arguments(BpnSchema)
    @blp.response(201, BpnSchema)
    def post(self, user_data):
        store = BpnModel(**user_data)
        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(400, message="same phone number exist")    
        except SQLAlchemyError:
            abort(500, message="an error occured while inserting bpn")

        return store       