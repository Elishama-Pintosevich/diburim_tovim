
import json
from datetime import datetime




#resp, number, start_play="", end_play=""
def redirect_to_asistent(**kwargs):

    kwargs.get('resp').play(kwargs.get('start_play'))
    kwargs.get('resp').dial(caller_id=kwargs.get('identity'))
    kwargs.get('resp').play(kwargs.get('end_play'))
    kwargs.get('resp').hangup()
    
    
#resp, play=""
def return_to_main(**kwargs):

    kwargs.get('resp').play(kwargs.get('play'))
    kwargs.get('resp').redirect(f'/ivr?retry=yes&phone_number={kwargs.get('bpn')}')
    
#resp, gather, play=""
def play_and_gather(**kwargs):

    kwargs.get('gather').play(kwargs.get('play'))
    kwargs.get('resp').append(kwargs.get('gather'))
   
    
#resp, play=""
def play(**kwargs):

    kwargs.get('resp').play(kwargs.get('play'), loop=3)
    kwargs.get('resp').hangup()
    
def check_nearest_end_week(**kwargs):
    today = (datetime.now().isoweekday() % 7)+1
    remainUntil5 = (5 - today) % 7 
    
    date = datetime(datetime.now().year, datetime.now().month, datetime.now().day + remainUntil5)
    # date = f'{datetime.now().year}-{datetime.now().month}-{datetime.now().day + remainUntil5}'
    
    # is_reserved = any(d.taken_date == date.strftime("%Y-%m-%d") for d in kwargs.get('dates'))
    is_reserved = False
    for d in kwargs.get('dates'):
        print(d.taken_date)
        if d.taken_date == date.strftime("%Y-%m-%d"):
            is_reserved = True
            break
    
    # print(date)
    # print(list(kwargs.get('dates')))
    print(date.strftime("%Y-%m-%d"))
    print(remainUntil5)
    print(is_reserved)
    kwargs.get('resp').say('its reserve, thank you.') if is_reserved else kwargs.get('resp').say('its not reserve, , thank you.')

    kwargs.get('resp').hangup()
    



def call_by_path_action_type(path, actions, resp, gather, bpn, client, dates):
    func_list = [redirect_to_asistent, return_to_main, play_and_gather, play, check_nearest_end_week]
    filtered_list = list(filter(lambda d: d.path == path, actions))
    if len(filtered_list) > 0:
        my_sounds = filtered_list[0].sounds[:]
        my_dict = {d.type: f'https://storage.googleapis.com/sound-storage/{d.path}' for d in my_sounds}
        my_dict['identity'] = filtered_list[0].parameters or None
        func_list[filtered_list[0].kind](resp = resp, gather = gather, bpn = bpn, client = client, dates = dates, **my_dict)
        return True
    else:
        return False
       
    