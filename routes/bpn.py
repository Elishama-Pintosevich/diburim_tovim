from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from models import BpnModel
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
# from db import stores
from schemas import BpnSchema, BpnBaseSchema

blp = Blueprint("bpn", __name__, description = "bpn controller")

@blp.route("/bpnByPhoneNumber/<string:bpn>")
class BpnByNumber(MethodView):
    @blp.doc(parameters=[{'name': 'bpn','in': 'path','description': 'The business phone number of the user','required': True,'schema': {'type': 'string'}}])
    @blp.response(200, BpnSchema)
    def get(self, bpn):
        item = BpnModel.query.filter_by(phone_number = bpn).first_or_404()
        return item
    
@blp.route("/bpn/<int:item_id>")
class BpnItem(MethodView):   
    @blp.doc(parameters=[{'name': 'item_id','in': 'path','description': 'The ID of the user','required': True,'schema': {'type': 'integer'}}])
    @blp.response(200, BpnSchema)
    def get(self, item_id):
        item = BpnModel.query.get_or_404(item_id)
        return item 
    
    @blp.doc(parameters=[{'name': 'item_id','in': 'path','description': 'The ID of the user','required': True,'schema': {'type': 'integer'}}])
    def delete(self, item_id):
        item = BpnModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"msg":"user deleted"}
    
    @blp.doc(parameters=[{'name': 'item_id','in': 'path','description': 'The ID of the user','required': True,'schema': {'type': 'integer'}}])
    @blp.arguments(BpnBaseSchema)
    @blp.response(200, BpnSchema)
    def put(self, item_data, item_id):
        item = BpnModel.query.get_or_404(item_id)

        item.phone_number = item_data['phone_number']
        
        db.session.add(item)
        db.session.commit()

        return item
    
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