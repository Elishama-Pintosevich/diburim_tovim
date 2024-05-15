from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint
import os
from dotenv import load_dotenv
from twilio.twiml.voice_response import VoiceResponse, Gather


# from schemas import MailSend

def redirect_to_asistent(resp, number, start_play="", end_play=""):
    def inner():
        resp.say(start_play)
        resp.dial(number)
        resp.say(end_play)
        return str(resp)
    return inner

def return_to_main(resp, play=""):
    def inner():
        resp.say(play)
        resp.redirect('/ivr')
        return str(resp)
    return inner

def play_and_gather(resp, gather, play=""):
    def inner():
        gather.say(play)
        resp.append(gather)
        return str(resp)
    return inner

def play(resp, play=""):
    def inner():
        resp.say(play)
        return str(resp)
    return inner    




blp = Blueprint("ivr", __name__, description="api of ivr")
@blp.route("/ivr")
class Ivr(MethodView):
    def post(self):
        resp = VoiceResponse()
        gather = Gather(num_digits=1, action='/ivr2')
        start_func = play_and_gather(resp=resp, gather=gather, play='For tophia, press 1. For fantasy, press 2.')
        start_func()
        resp.redirect('/ivr')
        return str(resp)

        
@blp.route("/ivr2")
class Ivr2(MethodView):
    def post(self):
        resp = VoiceResponse()
        choice = int((request.values.get('Digits') or request.args.get('id') or 0)) - 1
        gather = Gather(num_digits=1, action=f'/ivr3?id={choice}')
        list_1 = [play_and_gather(resp=resp, gather=gather, play='You selected tophia. For check aviable, press 1. For Assistent press 2.'), play_and_gather(resp=resp, gather=gather, play='You selected fantasy. For check aviable, press 1. For Assistent press 2.')]
        if 'Digits' in request.values:
            if not (int(request.values.get('Digits')) > len(list_1) or int(request.values.get('Digits')) == 0):
                list_1[choice]()
            else:
                resp.say('wrong number')
                resp.redirect('/ivr') 
                return str(resp)   
        elif 'id' in request.args:
            list_1[choice]()

        resp.redirect(f'/ivr2?id={choice+1}')

        return str(resp)   
"""
http://localhost:5000/ivr3?id=0
"""
@blp.route("/ivr3")
class Ivr3(MethodView):
    def post(self):
        resp = VoiceResponse()
        id = int(request.args.get('id'))
        choice = int((request.values.get('Digits') or request.args.get('choise_id') or 0)) - 1
        gather = Gather(num_digits=1, action=f'/ivr4?id={id}&id2={choice}')
        list_2 = [[play_and_gather(resp=resp, gather=gather, play='You selected check aviable tophia. your date aviable. For Assistent press 1. For return to main menu press 2.'),
        redirect_to_asistent(resp=resp, number='972534905961', start_play='You need support. Elishama will Help you!', end_play='goodbye')],
        [play_and_gather(resp=resp, gather=gather, play='You selected check aviable fantasy. your date aviable. For Assistent press 1. For return to main menu press 2.'),
        redirect_to_asistent(resp=resp, number='972534905961', start_play='You need support. Elishama will Help you!', end_play='goodbye')]]

        if 'Digits' in request.values:
            if not (int(request.values.get('Digits')) > len(list_2[id]) or int(request.values.get('Digits')) == 0):
                list_2[id][choice]()
            else:
                resp.say('wrong number')
                resp.redirect(f'/ivr2?id={id+1}') 
                return str(resp) 
        elif 'choise_id' in request.args:
            list_2[id][choice]()

        resp.redirect(f'/ivr3?id={id}&choise_id={choice+1}')
        
        return str(resp)   
"""
http://localhost:5000/ivr4?id=0&id2=0
"""
@blp.route("/ivr4")
class Ivr4(MethodView):
    def post(self):
        resp = VoiceResponse()
        # gather = Gather(num_digits=1, action='/ivr3')
        list_3 = [[[redirect_to_asistent(resp=resp, number='972534905961', start_play='You need support. Elishama will Help you!', end_play='goodbye'),return_to_main(resp=resp)],[]],[[redirect_to_asistent(resp=resp, number='972534905961', start_play='You need support. Elishama will Help you!', end_play='goodbye'),return_to_main(resp=resp)],[]]]
        id = int(request.args.get('id'))
        id2 = int(request.args.get('id2'))
        choice = int(request.values['Digits']) - 1

        if 'Digits' in request.values:
            if not (int(request.values.get('Digits')) > len(list_3[id][id2]) or int(request.values.get('Digits')) == 0):
                list_3[id][id2][choice]()
            else:
                resp.say('wrong number')
                resp.redirect(f'/ivr3?id={id}&choise_id={id2+1}') 
                return str(resp) 
            
        resp.redirect('/ivr')
        return str(resp)   
        