from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint
import os
from dotenv import load_dotenv
from twilio.twiml.voice_response import VoiceResponse, Gather


# from schemas import MailSend
"""
מה שבעצם צריך לעשות זה שלוש מערכים ומשתנה עם פונקציה אחת
וגם מה שצריך לעשות זה זה ליצור פונקציות שיחזרו על עצמם בעצם ארבעה סוגים
1. פונקציה עם גטר שמקבלת את המספרים עם טקסט
2. פונקציה של דיבור בלבד 
3. פונקציה של רידיירקט לנציג שירות
4. פונקציה חזרה לתפריט הראשי

"""

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


# resp_1 = VoiceResponse()
# gather_1 = Gather(num_digits=1, action='/ivr2')

# resp_2 = VoiceResponse()
# gather_2 = Gather(num_digits=1, action='/ivr3')

# resp_3 = VoiceResponse()
# gather_3 = Gather(num_digits=1, action='/ivr4')


# start_func = play_and_gather(resp=resp_1, gather=gather_1, play='For tophia, press 1. For fantasy, press 2.')

# list_1 = [play_and_gather(resp=resp_2, gather=gather_2, play='You selected tophia. For check aviable, press 1. For Assistent press 2.'), play_and_gather(resp=resp_2, gather=gather_2, play='You selected fantasy. For check aviable, press 1. For Assistent press 2.')]

# list_2 = [[play_and_gather(resp=resp_3, gather=gather_3, play='You selected check aviable tophia. your date aviable. For Assistent press 1. For return to main menu press 2.'),
#            redirect_to_asistent(resp=resp_3, number='972534905961', start_play='You need support. Elishama will Help you!', end_play='goodbye')],
#            [play_and_gather(resp=resp_3, gather=gather_3, play='You selected check aviable fantasy. your date aviable. For Assistent press 1. For return to main menu press 2.'),
#            redirect_to_asistent(resp=resp_3, number='972534905961', start_play='You need support. Elishama will Help you!', end_play='goodbye')]]

# list_3 = [[[redirect_to_asistent(resp=resp_3, number='972534905961', start_play='You need support. Elishama will Help you!', end_play='goodbye'),return_to_main(resp=resp_3)],[]],[[redirect_to_asistent(resp=resp_3, number='972534905961', start_play='You need support. Elishama will Help you!', end_play='goodbye'),return_to_main(resp=resp_3)],[]]]


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
        if 'Digits' in request.values:
            choice = int(request.values['Digits']) - 1
            gather = Gather(num_digits=1, action=f'/ivr3?id={choice}')
            list_1 = [play_and_gather(resp=resp, gather=gather, play='You selected tophia. For check aviable, press 1. For Assistent press 2.'), play_and_gather(resp=resp, gather=gather, play='You selected fantasy. For check aviable, press 1. For Assistent press 2.')]
            list_1[choice]()

        resp.redirect('/ivr')

        return str(resp)   
"""
http://localhost:5000/ivr3?id=0
"""
@blp.route("/ivr3")
class Ivr3(MethodView):
    def post(self):
        resp = VoiceResponse()
        id = request.args.get('id')
        if 'Digits' in request.values:
            choice = request.values['Digits'] - 1
            gather = Gather(num_digits=1, action=f'/ivr4?id={id}&id2={choice}')
            list_2 = [[play_and_gather(resp=resp, gather=gather, play='You selected check aviable tophia. your date aviable. For Assistent press 1. For return to main menu press 2.'),
            redirect_to_asistent(resp=resp, number='972534905961', start_play='You need support. Elishama will Help you!', end_play='goodbye')],
            [play_and_gather(resp=resp, gather=gather, play='You selected check aviable fantasy. your date aviable. For Assistent press 1. For return to main menu press 2.'),
            redirect_to_asistent(resp=resp, number='972534905961', start_play='You need support. Elishama will Help you!', end_play='goodbye')]]
            list_2[id][choice]()

        resp.redirect('/ivr')
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

        if 'Digits' in request.values:
            id = request.args.get('id')
            id2 = request.args.get('id2')

            choice = request.values['Digits'] - 1
            list_3[id][id2][choice]()

        resp.redirect('/ivr')
        return str(resp)   
        