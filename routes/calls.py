from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models import UserModel
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VoiceGrant
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse, Gather
import os
from dotenv import load_dotenv
blp = Blueprint("Calls", __name__, description = "Calls controller")


@blp.route("/calls")
class Calls(MethodView):
    @blp.doc(parameters=[{'name': 'phone_number','in': 'query','description': 'The phone number to call','required': True,'schema': {'type': 'string'}},
                        {'name': 'identity','in': 'query','description': 'The identity','required': True,'schema': {'type': 'string'}}])
    def post(self):
        # load_dotenv()
        item = UserModel.query.filter_by(phone_number = request.args.get('phone_number')).first_or_404()
        account_sid = item.account
        api_key = item.api_key
        api_secret = item.api_secret
        identity = request.args.get('identity')
        CALLER_ID = 'client:quick_start'

        client = Client(api_key, api_secret, account_sid)
        to = request.values.get("to")
        call = None

        
        call = client.calls.create(url=request.url_root + '/ivr?phone_number=023764951', to='972534905961', from_='97223764951')
        
        return str(call)
        # resp = VoiceResponse()
        # # to = request.values.get("to")
        # # if to is None or len(to) == 0:
        # # print('good')
        # resp.play("https://storage.googleapis.com/sound-storage/mp3_files/test.mp3")
        # # elif to[0] in "+1234567890" and (len(to) == 1 or to[1:].isdigit()):
        # #     resp.dial(callerId='972534905961').number(to)
        # # else:
        # #     resp.dial(callerId=CALLER_ID).client(to)
        # return str(resp)

        


    
   

        