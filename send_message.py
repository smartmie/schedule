import get
import socket
import time
import draw_image
import draw_text
import datetime
import out_kb
def send_message (soc,t):
    send_data = draw_image.get_point_bin(draw_text.main(t))
    send_data = "{0}={1}={2}={3}".format(str(send_data.count(",")+1),"128","64",send_data)
    # print(send_data)
    while True:
        print('...')
        ip,address = soc.accept()
        print(ip,address)
        ip.send(bytes(send_data,encoding='utf-8'))
        break
    pass

def main_soc(host,port):
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # host = '192.168.1.110'
    # port = 5555
    soc.bind((host,port))
    print(host,port)
    soc.listen(5)
    return soc

# def output_schedule(find_text):
#     kb_schedule = get.main()

#     time_form = [
#     ["08:20","09:50"],
#     ["10:15","11:45"],
#     ["14:00","15:30"],
#     ["15:55","17:25"],
#   ]

#     # time_form_hour = [[],[],[],[]]
#     today_hour = time.localtime(time.time()).tm_hour
#     today_min = time.localtime(time.time()).tm_min
#     today_week = datetime.date.today().weekday() + 1

#     today_delta = datetime.timedelta(hours=today_hour,minutes = today_min)

    
#     count = 0
#     for t in time_form:
#         count += 2
#         h1,m1 = t[0].split(":")
#         h2,m2 = t[1].split(":")
#         print(h1,m1)
#         print(h2,m2)
#         one_time_delta = datetime.timedelta(hours = int(h1),minutes = int(m1))
#         two_time_delta = datetime.timedelta(hours = int(h2),minutes = int(m2))
#         if today_delta > one_time_delta and today_delta < two_time_delta :
#             find_text = "{0},{1}".format(str(today_week),str(count))
#             kb , time_schedule = get.find_schedule(find_text,kb_schedule)
#             break
#         elif count == 9:
#             return_text = "{0}\n{1}\n{2}".format("O(∩_∩)O休息哟","好好好玩",str(today_hour)+":"+str(today_min))
#             return return_text
        

#     print(kb) 
#     kb = "{0}\n{1}\n{2}".format(kb[0][0],kb[0][1],time_schedule)
#     return kb


if __name__ == "__main__":
    
    #             
    soc = main_soc('192.168.1.4',5555)
    send_message (soc,"一二三")
    pass