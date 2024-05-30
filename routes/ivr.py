from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint
import os
from dotenv import load_dotenv
from twilio.twiml.voice_response import VoiceResponse, Gather
from twilio.rest import Client
from services import send_mail, call_by_path_action_type
from models import BpnModel



"""
http://localhost:5000/ivr?phone_number=023764951
"""

"""

                                       ! change paramaters - parameters in actions model important !

"""
blp = Blueprint("ivr", __name__, description="api of ivr")
@blp.route("/ivr")
class Ivr(MethodView):
    @blp.doc(parameters=[{'name': 'phone_number','in': 'query','description': 'The phone number to call','required': True,'schema': {'type': 'string'}}])
    def post(self):

        resp = VoiceResponse()
        gather = Gather(num_digits=1, action=f'/ivr2?phone_number={request.args.get('phone_number')}')
        item = BpnModel.query.filter_by(phone_number = request.args.get('phone_number')).first_or_404()

        account_sid = item.user.account
        auth_token = item.user.token
        client = Client(account_sid, auth_token)
        calls = client.calls.list(to=request.args.get('phone_number'),limit=2)
        print(f"{account_sid} {auth_token}")
        print(calls)
        if not 'retry' in request.args:
            # send_mail({"subject":"לקוח חדש התעניין במוצר", "message":calls[0].from_formatted, "email":item.user.email})
            pass

        call_by_path_action_type('start', item.actions[:], resp, gather, request.args.get('phone_number'))

        resp.redirect(f'/ivr?retry=yes&phone_number={request.args.get('phone_number')}')
        return str(resp)

"""
http://localhost:5000/ivr2?phone_number=023764951
"""
@blp.route("/ivr2")
class Ivr2(MethodView):
    def post(self):
        resp = VoiceResponse()
        choice = int((request.values.get('Digits') or request.args.get('id') or 0)) - 1
        gather = Gather(num_digits=1, action=f'/ivr3?id={choice}&phone_number={request.args.get('phone_number')}')
        
        item = BpnModel.query.filter_by(phone_number = request.args.get('phone_number')).first_or_404()

        if 'Digits' in request.values:
           
            action = call_by_path_action_type(str(choice), item.actions, resp, gather, request.args.get('phone_number'))
          
            if not action:
                resp.say('wrong number')
                resp.redirect(f'/ivr?retry=yes&phone_number={request.args.get('phone_number')}') 
                return str(resp)   
            
        elif 'id' in request.args:
            
            call_by_path_action_type(str(choice), item.actions, resp, gather, request.args.get('phone_number'))


        resp.redirect(f'/ivr2?id={choice+1}&phone_number={request.args.get('phone_number')}')

        return str(resp)   
"""
http://localhost:5000/ivr3?id=0&phone_number=023764951
"""
@blp.route("/ivr3")
class Ivr3(MethodView):
    def post(self):
        resp = VoiceResponse()
        id = int(request.args.get('id'))
        choice = int((request.values.get('Digits') or request.args.get('choise_id') or 0)) - 1
        gather = Gather(num_digits=1, action=f'/ivr4?id={id}&id2={choice}&phone_number={request.args.get('phone_number')}')
        
        item = BpnModel.query.filter_by(phone_number = request.args.get('phone_number')).first_or_404()


        if 'Digits' in request.values:
            action = call_by_path_action_type(f"{id}.{str(choice)}", item.actions, resp, gather, request.args.get('phone_number'))
            
            if not action:
                resp.say('wrong number')
                resp.redirect(f'/ivr2?id={id+1}&phone_number={request.args.get('phone_number')}') 
                return str(resp) 
            
        elif 'choise_id' in request.args:
            call_by_path_action_type(f"{id}.{str(choice)}", item.actions, resp, gather, request.args.get('phone_number'))


        resp.redirect(f'/ivr3?id={id}&choise_id={choice+1}&phone_number={request.args.get('phone_number')}')
        
        return str(resp)   
"""
http://localhost:5000/ivr4?id=0&id2=0&phone_number=023764951
"""
@blp.route("/ivr4")
class Ivr4(MethodView):
    def post(self):
        resp = VoiceResponse()
        gather = Gather(num_digits=1, action='/ivr3')
        
        item = BpnModel.query.filter_by(phone_number = request.args.get('phone_number')).first_or_404()

        id = int(request.args.get('id'))
        id2 = int(request.args.get('id2'))
        choice = int(request.values['Digits']) - 1

        if 'Digits' in request.values:
            
            action = call_by_path_action_type(f"{id}.{id2}.{str(choice)}", item.actions, resp, gather, request.args.get('phone_number'))
           
            if not action:
                resp.say('wrong number')
                resp.redirect(f'/ivr3?id={id}&choise_id={id2+1}&phone_number={request.args.get('phone_number')}') 
                return str(resp) 
            
        resp.redirect(f'/ivr?retry=yes&phone_number={request.args.get('phone_number')}')
        return str(resp)   