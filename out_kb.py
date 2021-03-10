import datetime
import time
import get
def output_schedule(find_text):
    kb_schedule = get.main()

    time_form = [
    ["08:20","09:50"],
    ["10:15","11:45"],
    ["14:00","15:30"],
    ["15:55","17:25"],
  ]

    # time_form_hour = [[],[],[],[]]
    today_hour = time.localtime(time.time()).tm_hour
    today_min = time.localtime(time.time()).tm_min
    today_week = datetime.date.today().weekday() + 1

    today_delta = datetime.timedelta(hours=today_hour,minutes = today_min)

    
    count = 0
    for t in time_form:
        count += 2
        h1,m1 = t[0].split(":")
        h2,m2 = t[1].split(":")
        print(h1,m1)
        print(h2,m2)
        one_time_delta = datetime.timedelta(hours = int(h1),minutes = int(m1))
        two_time_delta = datetime.timedelta(hours = int(h2),minutes = int(m2))
        if today_delta > one_time_delta and today_delta < two_time_delta :
            find_text = "{0},{1}".format(str(today_week),str(count))
            kb , time_schedule = get.find_schedule(find_text,kb_schedule)
            kb = "{0}\n{1}\n{2}".format(kb[0][0],kb[0][1],time_schedule)
            print(kb)
            return kb
            
        
    count == 9
    return_text = "{0}\n{1}\n{2}".format("O(∩_∩)O休息哟","好好好玩",str(today_hour)+":"+str(today_min))
    return return_text
        

     
    