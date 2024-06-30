import mysql.connector
import json

from .file import *
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="chatbot"
)

db = mydb.cursor()

def reg_user(name,email,phone,dob,address,password,gender):
    sql = "INSERT INTO users (name,email,phone,dob,address,password,gender) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    val = (name,email,phone,dob,address,password,gender)
    db.execute(sql,val)
    if mydb.commit():

        return True
    return False

def verify(user,password):
    db.execute("SELECT * FROM users")
    myresult = db.fetchall()
    
    
    for x in myresult:
        if(x[1]==user and x[5]==password):
            print("Login Successful")
            return True
        else:
            print("Login Unsuccessful")
def get_name(str):
    db.reset()
    sql = "SELECT name FROM users where email='"+str+"'"
    
    db.execute(sql)
    myresult = db.fetchall()
    return myresult[0]

def get_holidays():
    db.execute("select * from holidays")
    result = db.fetchall()
    data = ""
    for x in result:
        data +=x[0]+" "+x[1]+"<br>"

    return data
#insert("om rajan rawool","om@gmail.com","7845785474","02-05-2003","kankavli","root")

def get_res():
    db.execute("select * from res")
    result = db.fetchall()
    data = "roll name class sub1 sub2 sub3 total<br>"
    for x in result:
        data +=x[0]+" "+x[1]+" "+x[2]+" "+x[3]+" "+x[4]+" "+x[5]+" "+x[6]+"<br>"

    return data

def get_my_res():
    name = read_file()
    db.execute("select * from res")
    result = db.fetchall()
    data=""
    for x in result:
        
        print(x[1])
        if x[1]==name:
            
            data +=x[0]+" "+x[1]+" "+x[2]+" "+x[3]+" "+x[4]+" "+x[5]+" "+x[6]+"<br>"
            break
    return data

def list_sch():
    db.execute("select * from schoolarship")
    result = db.fetchall()
    data=""
    for x in result:        
        data +=x[0]+" "+x[1]+"<br>"
    return data
       
def check_sch_res():
    name = read_file()
    db.execute("select * from schoolarshipres")
    data = db.fetchall()
    for x in data:
        print(x[0])
        if name in x[0]:
            print("schoolarship selection detected ")
            ret = "Congratulation &#129309<br>You are select in "+x[1]
            return ret
    return "Sorry<br> you didn't selected in any schoolarship<br>You can apply other schoolarships"
    
def sch_ins(namesc):
    name = read_file()
    db.execute("SELECT * FROM users")
    dat = db.fetchall()
    email = ""
    for x in dat:
        if name in x[0]:
            email=x[1]
            break
    sql = "INSERT INTO schapply (email,namesc) VALUES (%s,%s)"
    val = (email,namesc)
    db.execute(sql,val)
    mydb.commit()
    return True
    
def all_sch_res():
    db.execute("SELECT * FROM schoolarshipres")
    dat = db.fetchall()
    ret=""
    for x in dat:
        ret+=x[0]+" "+x[1]+"<br>"
    return ret

def get_email():
    name = read_file()
    db.execute("select * from users where name = '"+name+"'")
    rest=db.fetchall()
    return rest

def update_pass(password):
    id = get_email()[0][1]
    print(id)
    db.execute("update users set password = '"+password+"' where email = '"+id+"'")
    mydb.commit()
    return True
    
def new_admission():
    id = get_email()[0][1]
    db.execute("select * from users")
    res = db.fetchall()
    for x in res:
        if x[1]==id:
            sql = "INSERT INTO newadd (name,email,phone,dob,address,gender) VALUES (%s,%s,%s,%s,%s,%s)"
            val = (x[0],x[1],x[2],x[3],x[4],x[6])
            db.execute(sql,val)
            mydb.commit()
            print("True")
            break

def canaddmission():
    id = get_email()[0][1]
    db.execute("delete from newadd where email = '"+id+"'")
    mydb.commit()

def get_fee():
    data = "faculty course lab library event total<br>"
    db.execute("select * from feestr")
    res = db.fetchall()
    
    for x in res:
        data +=x[0]+" "+x[1]+" "+x[2]+" "+x[3]+" "+x[4]+" "+x[5]+"<br>"
    return data


def verify_email(email):
    db.execute("SELECT * FROM users")
    myresult = db.fetchall()

    for x in myresult:
        print(x[1])
        if(x[1]==email): 
            print("email found in database")
            return True
    return False
    print("email not found on database")
    

def change_pass(passw):
    email = read_file()
    db.execute("update users set password = '"+passw+"' where email = '"+email+"'")
    mydb.commit()
    return True


def get_staff(faculty):
    db.execute("select * from staff where faculty = '"+faculty+"'")
    res = db.fetchall()
    ret = "Name&nbsp;&nbsp;&nbsp;&nbsp; Phone&nbsp;&nbsp;&nbsp;&nbsp; Faculty Name<br>"
    for x in res:
        ret+=x[0]+"&nbsp;&nbsp;"+x[1]+"&nbsp;&nbsp;"+x[2]+"<br>"

    return ret

def get_count(tab_name,type):
    db.execute(f"select * from {tab_name}")
    res = db.fetchall()
    ret = "We have currently "+str(len(res))+ " "+type+""

    return ret


def timetable(faculty):
    sql = "select * from tablename where class in "+str(faculty)
    print(faculty)
    print(sql)
    db.execute(sql)
    res = db.fetchall()
    ret = f"""<table border="1">
       <tr>
            <th> Class</th>
            <th> Time</th>
            <th> Mon</th>
            <th> Tue</th>
            <th> Wed</th>
            <th> Thu</th>
            <th> Fri</th>
            <th> Sat</th>
       </tr>"""
    for x in res:
        ret+=f"""<tr>
            <td>{x[0]}</td>
            <td>{x[1]}</td>
            <td>{x[2]}</td>
            <td>{x[3]}</td>
            <td>{x[4]}</td>
            <td>{x[5]}</td>
            <td>{x[6]}</td>
            <td>{x[7]}</td>
       </tr>"""
        
    ret +="</table>"
    return ret