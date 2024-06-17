from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models import UserModel
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VoiceGrant

blp = Blueprint("token", __name__, description = "token controller")


@blp.route("/token/<string:pn>")
class Token(MethodView):
    @blp.doc(parameters=[{'name': 'pn','in': 'path','description': 'The phone number of the user','required': True,'schema': {'type': 'string'}}])
    @blp.response(200)
    def get(self, pn):
        item = UserModel.query.filter_by(phone_number = pn).first_or_404()
        account_sid = item.account
        api_key = item.api_key
        api_secret = item.api_secret
        identity = pn

        token = AccessToken(account_sid, api_key, api_secret, identity=identity)
        voice_grant = VoiceGrant(
            incoming_allow=True
        )
        token.add_grant(voice_grant)

        return token.to_jwt()
    