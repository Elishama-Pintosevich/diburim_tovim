from datetime import datetime

# Assuming you have a date variable
date_variable = datetime(2024, 7, 16)  # Example date

# Get the day of the week
day_of_week = date_variable.weekday() # '%A' gives the full weekday name

print(f"The day of the week for {date_variable.date()} is {day_of_week}.")

date_list = [datetime(2024, 7, 15),datetime(2024, 7, 16),datetime(2024, 7, 17),datetime(2024, 7, 18),datetime(2024, 7, 19),datetime(2024, 7, 20),
             datetime(2024, 7, 21),datetime(2024, 7, 22),datetime(2024, 7, 23),datetime(2024, 7, 24),datetime(2024, 7, 24),datetime(2024, 7, 26),
             datetime(2024, 7, 27)]

def check_nearest_end_week_exist(dates):
    
    today = (datetime.now().isoweekday() % 7)+1
    # today = 7
    remainUntil5 = (5 - today) % 7 #אם זה יום שישי מה עושים - 6 זה בעצם עוד 6 ימים אם זה שבת אז עוד 5 ימים אולי לעשות מינוס 7 אם זה 1 אז זה יהיה מינוס
    #מינוס 6 ןעוד 5 זה 11 מודולו 7 זה 4 
    print(remainUntil5)
    date = datetime(datetime.now().year, datetime.now().month, datetime.now().day + remainUntil5)
    # date = datetime(datetime.now().year, datetime.now().month, 14 + remainUntil5)
    print(date.date())

    return date in dates
    
check = check_nearest_end_week_exist(date_list)
print(check)