
import json




#resp, number, start_play="", end_play=""
def redirect_to_asistent(**kwargs):
    kwargs.get('resp').say(kwargs.get('start_play'))
    kwargs.get('resp').dial(kwargs.get('number'))
    kwargs.get('resp').say(kwargs.get('end_play'))
    kwargs.get('resp').hangup()
    
    
#resp, play=""
def return_to_main(**kwargs):
    kwargs.get('resp').say(kwargs.get('play'))
    kwargs.get('resp').redirect(f'/ivr?retry=yes&phone_number={kwargs.get('bpn')}')
    
#resp, gather, play=""
def play_and_gather(**kwargs):
    kwargs.get('gather').say(kwargs.get('play'))
    kwargs.get('resp').append(kwargs.get('gather'))
   
    
#resp, play=""
def play(**kwargs):
    kwargs.get('resp').say(kwargs.get('play'), loop=3)
    kwargs.get('resp').hangup()
    
        



def call_by_path_action_type(path, actions, resp, gather, bpn):
    func_list = [redirect_to_asistent, return_to_main, play_and_gather, play]
    filtered_list = list(filter(lambda d: d.path == path, actions))
    if len(filtered_list) > 0:
        my_dict = json.loads(filtered_list[0].paramaters)
        func_list[filtered_list[0].kind](resp = resp, gather = gather, bpn = bpn, **my_dict)
        return True
    else:
        return False
       
    