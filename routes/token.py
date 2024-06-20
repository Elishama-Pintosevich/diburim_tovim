from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models import UserModel
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VoiceGrant
import os
from dotenv import load_dotenv
blp = Blueprint("token", __name__, description = "token controller")


@blp.route("/token")
class Token(MethodView):
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
        push_credential_sid= os.environ['PUSH_CREDENTIAL_SID']
        outgoing_application_sid=os.environ['APP_SID']

        token = AccessToken(account_sid, api_key, api_secret, identity=identity)
        voice_grant = VoiceGrant(
            push_credential_sid=push_credential_sid,
            outgoing_application_sid=outgoing_application_sid
        )
        token.add_grant(voice_grant)

        return token.to_jwt()
    