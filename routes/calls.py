from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models import UserModel
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VoiceGrant
from twilio.rest import Client
import os
from dotenv import load_dotenv
blp = Blueprint("Calls", __name__, description = "Calls controller")


@blp.route("/calls")
class Calls(MethodView):
    @blp.doc(parameters=[{'name': 'phone_number','in': 'query','description': 'The phone number to call','required': True,'schema': {'type': 'string'}},
                        {'name': 'identity','in': 'query','description': 'The identity','required': True,'schema': {'type': 'string'}}])
    @blp.response(200)
    def get(self):
        load_dotenv()
        item = UserModel.query.filter_by(phone_number = request.args.get('phone_number')).first_or_404()
        account_sid = item.account
        api_key = item.api_key
        api_secret = item.api_secret
        identity = request.args.get('identity')
        CALLER_ID = 'client:quick_start'

        client = Client(api_key, api_secret, account_sid)
        to = request.values.get("to")
        call = None

        if to is None or len(to) == 0:
            call = client.calls.create(url=request.url_root + 'ivr?phone_number=023764951', to='client:' + identity, from_=CALLER_ID)
        elif to[0] in "+1234567890" and (len(to) == 1 or to[1:].isdigit()):
            call = client.calls.create(url=request.url_root + 'ivr?phone_number=023764951', to=to, from_='972534905961')
        else:
            call = client.calls.create(url=request.url_root + 'ivr?phone_number=023764951', to='client:' + to, from_=CALLER_ID)
        return str(call)

        


    
   

        