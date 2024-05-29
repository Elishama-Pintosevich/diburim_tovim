"""
מה שאני צריך לעשות זה פונקציה שבעצם אני נותן לה את הרמה ולפי זה היא מסננת לי אותם הבעיה למשל רמה 3 איך היא תדע לסווג אותם אולי לעשות דרך שבנוי מי 
1.1.1
מסטרינג ובעצם לפי זה אני אדע איך לסדר אותו, ובעצם אפשר לא לעבוד עם מערך אלא אם המשתמש הקיש 1 אז נותנים לו פונקציה עם דרך 1 עם 1.2 אז נותנים לו פונקציה עם הדרך הזאת ולפי זה אפשר לתת איזה מקש שבא לנו 
אז בעצם מה שיקרה כל רמה ניצור דרך ונשלח לפונקציה לזאת אם יש כזה דרך הוא ישלח משהו אם לא אז יהיה טעות
אז בעצם יהיה פרמטר של דרך ופרמטר של מערך האקשנס והוא יבדוק את איזה אקשן תואם ולפי הסוג ידע לבחור איזה פונקציה להחזיר 
"""
def redirect_to_asistent(resp, number, play="", end_play=""):
    def inner():
        # resp.say(start_play)
        # resp.dial(number)
        # resp.say(end_play)
        print(play)
        print("asistent")
    return inner

def return_to_main(resp, play=""):
    def inner():
        # resp.say(play)
        # resp.redirect('/ivr?retry=yes')
        print(play)
        print("main")
    return inner

def play_and_gather(resp, gather, play=""):
    def inner():
        # gather.say(play)
        # resp.append(gather)
        print(play)
        print("gather")
    return inner

def play(resp, play=""):
    def inner():
        # resp.say(play)
        print(play)
        print("play")
    return inner    

mock_list = [
        {
        "id": 0,
        "path": "1",
        "kind": 1,
        "paramaters": {"play":"hello"}
        },
        {
        "id": 0,
        "path": "1.2",
        "kind": 1,
        "paramaters": {"play":"hello"}
        },
        {
        "id": 0,
        "path": "3.3",
        "kind": 2,
        "paramaters": {"play":"hello"}
        }
    ]
def call_by_path_action_type(path, actions, resp):
    #any(path == dictionary['path'] for dictionary in actions):
    func_list = [redirect_to_asistent, return_to_main, play_and_gather, play]
    filtered_list = list(filter(lambda d: d.get('path') == path, actions))
    if len(filtered_list) > 0:
        return func_list[filtered_list[0].get('kind')](resp, play="hi")
    
       
    
        
call_by_path_action_type("1.2", mock_list, "hi")()