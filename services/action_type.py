from text_to_speech import get_speech_from_text
import json




#resp, number, start_play="", end_play=""
def redirect_to_asistent(**kwargs):

    start_play = get_speech_from_text(kwargs.get('start_play'))

    kwargs.get('resp').play(start_play)
    kwargs.get('resp').dial(kwargs.get('number'))

    end_play = get_speech_from_text(kwargs.get('end_play'))

    kwargs.get('resp').play(end_play)
    kwargs.get('resp').hangup()
    
    
#resp, play=""
def return_to_main(**kwargs):

    play = get_speech_from_text(kwargs.get('play'))

    kwargs.get('resp').play(play)
    kwargs.get('resp').redirect(f'/ivr?retry=yes&phone_number={kwargs.get('bpn')}')
    
#resp, gather, play=""
def play_and_gather(**kwargs):

    play = get_speech_from_text(kwargs.get('play'))

    kwargs.get('gather').play(play)
    kwargs.get('resp').append(kwargs.get('gather'))
   
    
#resp, play=""
def play(**kwargs):

    play = get_speech_from_text(kwargs.get('play'))

    kwargs.get('resp').play(play, loop=3)
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
       
    