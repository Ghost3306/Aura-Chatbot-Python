import mysql.connector
import random
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="chatbot"
)
db = mydb.cursor()

names = ["Advik","Atharv","Vihaan","Kiaan","Shivansh",'Rishaan','Ayansh','Viraj','Aryan','Arjun','Dhruv','Ayaan','Yuvaan','Rudra','Kabir','Mikayl','Aarush','Kartik','Avyaan','Sai','Hridaan','Ishan']
sirnames= ['Jadhav', 'Gaikwad', 'Lokhande', 'Rane', 'Kambli', 'Mhatre', 'Sawant', 'Bhosale', 'Gokhale', 'Agarkar', 'Mankar', 'Patil', 'Kadam', 'Joshi', 'Shinde', 'Gaetonde', 'Kamble', 'More', 'Ingle']
faculty = ["BCom","BSc","BA"]

random_index_name = random.randint(0,len(names)-1)
random_index_sirname = random.randint(0,len(sirnames)-1)

def generate_random_number():
    return str(random.randint(7895876987,9999987895))

for i in range(7):
    
    name = str(names[random.randint(0,len(names)-1-1-1)])+' '+str(sirnames[random.randint(0,len(sirnames)-1)])
    phone = generate_random_number()
    faculty_name = "BCom"
    sql = "insert into staff (name,phone, faculty) VALUES('"+name+"','"+phone+"','"+faculty_name+"')"
    val = (name,phone,faculty)
    db.execute(sql)
    mydb.commit()

for i in range(5):
    
    name = str(names[random.randint(0,len(names)-1)])+' '+str(sirnames[random.randint(0,len(sirnames)-1)])
    phone = generate_random_number()
    faculty_name = "Bsc"
    sql = "insert into staff (name,phone, faculty) VALUES('"+name+"','"+phone+"','"+faculty_name+"')"
    val = (name,phone,faculty)
    db.execute(sql)
    mydb.commit()
  
for i in range(5):
    
    name = str(names[random.randint(0,len(names)-1)])+' '+str(sirnames[random.randint(0,len(sirnames)-1)])
    phone = generate_random_number()
    faculty_name = "BSc CS"
    sql = "insert into staff (name,phone, faculty) VALUES('"+name+"','"+phone+"','"+faculty_name+"')"
    val = (name,phone,faculty)
    db.execute(sql)
    mydb.commit()

for i in range(5):
    
    name = str(names[random.randint(0,len(names)-1)])+' '+str(sirnames[random.randint(0,len(sirnames)-1)])
    phone = generate_random_number()
    faculty_name = "BA"
    sql = "insert into staff (name,phone, faculty) VALUES('"+name+"','"+phone+"','"+faculty_name+"')"
    val = (name,phone,faculty)
    db.execute(sql)
    mydb.commit()