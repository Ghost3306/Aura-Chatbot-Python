import smtplib  
import random   
from .file import *

def send_mail(message):
    sender_mail = 'lrrawool2503@gmail.com'    
    receivers_mail = ['lalitrawool25@gmail.com']          
    password = "vpbursndolfqzlgq" 
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender_mail, password)
    s.sendmail(sender_mail, receivers_mail, message)
    s.quit()
    print("mail send successful")
    return True


def email_send(email,message):
    sender_mail = 'lrrawool2503@gmail.com'    
          
    password = "vpbursndolfqzlgq" 
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender_mail, password)
    s.sendmail(sender_mail, email, message)
    s.quit()
    print("mail send successful")
    return True

def send_otp():
    otp = str(random.randint(1111,9999) ) 
    write_otp(otp)
    data = "Send this otp to Aura chatbot to verify\nand continue to update password\n"+otp+"\nDO NOT SHARE!!"
    return data
