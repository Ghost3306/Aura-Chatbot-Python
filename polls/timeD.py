import datetime
import time
import random
from datetime import date
time = datetime.datetime.now()

def current_hour():
    return time.strftime("%H")
tm =int(current_hour())

def time_now():
    return time.strftime("It's a %H:%M clock")
def date_now():
    return "Today's date is "+str(date.today())

def datetime_now():
    return "Date Time is "+str(date.today())+", "+time.strftime("%H:%M")
    

def check_gm():
    print("tm",tm)
    true_res_gm = ["Yeah have a good morning you to &#127748;","yeah thanks good morning","Gooood Morning &#127748;","Good morning to you"]
    false_res_gm= ["Thanks but you need to wake up early &#128514;","well I am not considering this time as morning &#128522;","Thanks but not thanks","Just for humour check your clock please"]
    
    if tm>5 and tm<12:
        
        return true_res_gm[random.randint(0,3)]
    else:
        
        return false_res_gm[random.randint(0,3)]

def check_gn():
    print("tm",tm)
    true_res_gn = ["Yeah have a good night you to &#127747;","yeah thanks good night have sweet dreams &#127750;","Good Night Sweet Dreams Take Care &#127747;","Good Night to you"]
    false_res_gn= ["Thanks but I can't see moon","well I am not considering this time as night &#128514;","Thanks but not thanks &#128522;","Just for humour go outside"]
    if tm>17 and tm<25:
        
        return true_res_gn[random.randint(0,3)]
        
    else:
     
        return false_res_gn[random.randint(0,3)]





def check_ga():
    print("tm",tm)
    true_res_ga = ["Good Afternoon;","Good Day","Afternoon did you hava a lunch?","Good Day to you"]
    false_res_ga= ["Thanks but I but its not afternon","well I am not considering this time as aftenoon","Thanks but not thanks &#128522;","Just for humour check the time "]
    
    if tm>12 and tm<16:
       
        return true_res_ga[random.randint(0,3)]
    else:
        
        return false_res_ga[random.randint(0,3)]

def check_ge():
    print("tm",tm)
    true_res_ge = ["Good Evening;","Good Evenind..<br>isn't it beuatiful sunset","Evening have you drink tea?","Good Eveening"]
    false_res_ge= ["Thanks but I there are some time for evening","well you can consider it evening I am not","Thanks but not thanks &#128522;","I think it not time for tea"]
    
    if tm>17 and tm<20:
        
        return true_res_ge[random.randint(0,3)]
    else:
        
        return false_res_ge[random.randint(0,3)]


