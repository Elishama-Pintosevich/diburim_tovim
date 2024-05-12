from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint
import os
from dotenv import load_dotenv
from twilio.twiml.voice_response import VoiceResponse, Gather


# from schemas import MailSend


blp = Blueprint("ivr", __name__, description="api of ivr")

@blp.route("/ivr")
class Ivr(MethodView):
    def post(self):
        resp = VoiceResponse()
        # Start our <Gather> verb
        gather = Gather(num_digits=1, action='/ivrGather')
        gather.say('For sales, press 1. For support, press 2.')
        resp.append(gather)
        resp.redirect('/ivr')

        return str(resp)
# def post(self):
    #     resp = VoiceResponse()

    #     # Read a message aloud to the caller
    #     resp.say("Thank you for calling! you redirect to Elishama Pintosevich.", voice='Polly.Amy')
    #     resp.dial('972534905961')
    #     resp.say("goodbye")
    #     return str(resp)
        
@blp.route("/ivrGather")
class IvrGather(MethodView):
    def post(self):
        resp = VoiceResponse()

        if 'Digits' in request.values:
            
            choice = request.values['Digits']
            if choice == '1':
                resp.say('You selected sales. Good for you!')
                resp.redirect('/ivr')
                return str(resp)
            elif choice == '2':
                resp.say('You need support. Elishama will Help you!')
                resp.dial('972534905961')
                resp.say("goodbye")
                return str(resp)
            else:
                # If the caller didn't choose 1 or 2, apologize and ask them again
                resp.say("Sorry, I don't understand that choice.")

        # If the user didn't choose 1 or 2 (or anything), send them back to /voice
        resp.redirect('/ivr')

        return str(resp)   
        
        






