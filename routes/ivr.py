from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint
import os
from dotenv import load_dotenv
from twilio.twiml.voice_response import VoiceResponse


# from schemas import MailSend


blp = Blueprint("ivr", __name__, description="api of ivr")

@blp.route("/ivr")
class Ivr(MethodView):
    @blp.response(200)
    def post(self):
        resp = VoiceResponse()

        # Read a message aloud to the caller
        resp.say("Thank you for calling! Have a great day.", voice='Polly.Amy')

        return str(resp)
        






