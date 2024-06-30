import os
from pathlib import Path
BASE_DIR = str(Path(__file__).resolve().parent.parent)
def write_file(username):
    pat = BASE_DIR+"\\writable\\user.txt"
    f= open(pat,"w")
    f.write(username) 
    f.close()
    

def read_file():
    pat = BASE_DIR+"\\writable\\user.txt"
    f= open(pat,"r")   
    contents =f.read()
    return contents

def write_otp(otp):
    pat = BASE_DIR+"\\writable\\otp.txt"
    f= open(pat,"w")
    f.write(otp) 
    f.close()


def read_otp():
    pat = BASE_DIR+"\\writable\\otp.txt"   
    f= open(pat,"r")
    contents =f.read()
    return contents

def write_status(str):
    pat = BASE_DIR+"\\writable\\status.txt"
    f= open(pat,"w")
    f.write(str) 
    f.close()

def read_status():
    pat = BASE_DIR+"\\writable\\status.txt"
    f= open(pat,"r")   
    contents =f.read()
    return contents