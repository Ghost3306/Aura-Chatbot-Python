from django.shortcuts import render
from django.http import *
from django.contrib import auth
from django.contrib.auth.models import User
from polls import CrMLData 
from .CrMLData import *
from django.utils import timezone
from .db import *
from .file import *
from .send_mail import *
from .timeD import *
from django.contrib.messages import constants as messages
from django.contrib import messages

# Create your views here.
name = "not found"
def chat(request):
    d = read_status()
    if d =="false":
        return HttpResponseRedirect("login")
    user = read_file()
    print("user",user)
    nameF = ""
    for i in user:
        if i == " ":
            break
        nameF+=i
    data = {
        'username':user,
        'name':nameF
    }
    if request.method == 'POST':
        message = request.POST.get('message')

        print("Entered Message is : ",message)
        word = "subject : complaint"
        if word in message:
            if send_mail(message):
                res =['Your complaint send successful', 'ret']
                return JsonResponse({'message': message, 'response': res})
        if "schoolarship name" in message:
            scname=message.replace("schoolarship name : "," ")
            rs = sch_ins(scname)
            if rs:
                res =['Your application submitted successful', 'ret']
                return JsonResponse({'message': message, 'response': res})
        
        

        if len(message)==4:
            print("otp detected")
            otp = read_otp()
            if message==otp:
                res =['Enter your new password below', 'getpass']
                return JsonResponse({'message': message, 'response': res})
        if "password : " in message:
            passw= message.replace("password : ","")  
            print("new password is",passw)
            update_pass(passw)
            res =['Your password update successfully', 'passup']
            return JsonResponse({'message': message, 'response': res})
        if "Suggestion" in message:
            if send_mail(message):
                res =['I will implement your suggestion', 'ret']
                return JsonResponse({'message': message, 'response': res})

        if "Issue" in message:
            if send_mail(message):
                res =["I've try to fix your issues", 'ret']
                return JsonResponse({'message': message, 'response': res})
            
        if "Feedback" in message:
             if send_mail(message):
                arr = ['Your feedback send successfully','Your response matters to us',
                       'Your feedback considerably helps us','Thanks for your feedback']
                res =[arr[random.randint(0,len(arr)-1)], 'ret']
                return JsonResponse({'message': message, 'response': res})


        res = response(message)
        tag = res[1]
        print("tag :",tag)
        if tag =="holiday":
             data = get_holidays()
             print("data received",data)
             return JsonResponse({'message': message, 'response': res,'holidays':data})
        if tag=="resultall":
            data = get_res()
            return JsonResponse({'message': message, 'response': res,'result':data})
        if tag =="resultme":
            data = get_my_res()
            print("my result",data)
            return JsonResponse({'message': message, 'response': res,'result':data})
        if tag=="schoolarshipadd":
            ret = "Here a list <br>"+list_sch()
            res = [ret,tag]
            #res =[ret, tag]
            
            return JsonResponse({'message': message, 'response': res,'result':data})
        if tag=="mySchoolarshipRes":
            res = [check_sch_res(),tag]
            return JsonResponse({'message': message, 'response': res})
    
        if tag=="allSchoolarshipRes":
            res = [all_sch_res(),tag]
            return JsonResponse({'message': message, 'response': res})
        
        if tag=="resetpass":
            id = get_email()[0][1]
            data = send_otp()
            email_send(id,data)
            print(id,data)
        if tag=="admission":
            new_admission()
            res = ["You enrolledment is successful\nYou will be inform for further information",tag]
            return JsonResponse({'message': message, 'response': res})
        
        if tag=="canadmission":
            canaddmission()
            res = ["Your admission cancel successfully",tag]
            return JsonResponse({'message': message, 'response': res})
        if tag=="feestructure":
            ret = "Heres a result<br>"+get_fee()
            res = [ret,tag]
            return JsonResponse({'message': message, 'response': res,'fee':data})
        if tag=="fascility":
            res=["Heres what we offers","Cafeteria","Library","Laboratory","Big ground","Sports",
                 "Computer Lab","Internet over campus","Campus Interview","fascility"]
            return JsonResponse({'message': message, 'response': res})
        
        if tag == "morning":
            res = [check_gm(),tag]
            return JsonResponse({'message': message, 'response': res})
        if tag == "afternoon":
            res = [check_ga(),tag]
            return JsonResponse({'message': message, 'response': res})
        if tag == "evening":
            res = [check_ge(),tag]
            return JsonResponse({'message': message, 'response': res})
        if tag == "night":
            res = [check_gn(),tag]
            return JsonResponse({'message': message, 'response': res})
        
        #detecting extra basic features 
        if tag == "time":
            res=[time_now(),tag]
            return JsonResponse({'message': message, 'response': res})
        if tag == "date":
            res=[date_now(),tag]
            return JsonResponse({'message': message, 'response': res})
        if tag == "datetime":
            res=[datetime_now(),tag]
            return JsonResponse({'message': message, 'response': res})

        if tag =='fybas':
            res=["FyBA syllabus below <br> <a href='https://drive.google.com/file/d/1O_PaIna-kBNuoRNoyVITPrrbbjuP3NI5/view?usp=drive_link'>Click Here</a>",tag]
            return JsonResponse({'message': message, 'response': res})

        if tag =='sybas':
            res=["SyBA syllabus below <br> <a href='https://drive.google.com/file/d/1AGY9UL4CJuRzYsFiLm9AGMHJuz4W7BQF/view?usp=drive_link'>Click Here</a>",tag]
            return JsonResponse({'message': message, 'response': res})
        
        if tag =='tybas':
            res=["TyBA syllabus below <br> <a href='https://drive.google.com/file/d/1adroGmtEkETZAwmA0-q7r_wYCYzX5U_9/view?usp=drive_link'>Click Here</a>",tag]
            return JsonResponse({'message': message, 'response': res})
        
        if tag =='fybcoms':
            res=["FyBcom syllabus below <br> <a href='https://drive.google.com/file/d/1BjL2QQ3CNt8NIC4peYKcaQOtB3U1JpwV/view?usp=drive_link'>Click Here</a>",tag]
            return JsonResponse({'message': message, 'response': res})

        if tag =='sybcoms':
            res=["SyBcom syllabus below <br> <a href='https://drive.google.com/file/d/19-zXVzZBYzte_d2Ef2pnAkBnZfZQlEzy/view?usp=drive_link'>Click Here</a>",tag]
            return JsonResponse({'message': message, 'response': res})
        
        if tag =='tybcoms':
            res=["TyBcom syllabus below <br> <a href='https://drive.google.com/file/d/1OwF2KapOI_7FAs7is-k0Dunw20mFmpE3/view?usp=drive_link'>Click Here</a>",tag]
            return JsonResponse({'message': message, 'response': res})

        if tag =='fybscs':
            res=["FyBsc syllabus below <br> <a href='https://drive.google.com/file/d/12LmM6xFuWuwKRuGPWQSxCNDCW61e7HTS/view?usp=drive_link'>Click Here</a>",tag]
            return JsonResponse({'message': message, 'response': res})

        if tag =='sybscs':
            res=["SyBsc syllabus below <br> <a href='https://drive.google.com/file/d/1-RsYxVDNWLsi1UnEBqgSHeGH0fy18Efd/view?usp=drive_link'>Click Here</a>",tag]
            return JsonResponse({'message': message, 'response': res})
        
        if tag =='tybscs':
            res=["TyBsc syllabus below <br> <a href='https://drive.google.com/file/d/17Yitf0ZjZriO-r79qYeunS2JzKcw4l_T/view?usp=drive_link'>Click Here</a>",tag]
            return JsonResponse({'message': message, 'response': res})

        if tag =='fybsccss':
            res=["FyBscCS syllabus below <br> <a href='https://drive.google.com/file/d/1FDCEgsVxVV6VN8bl8x6nl9pKlHwa8jND/view?usp=drive_link'>Click Here</a>",tag]
            return JsonResponse({'message': message, 'response': res})

        if tag =='sybsccss':
            res=["SyBscCS syllabus below <br> <a href='https://drive.google.com/file/d/1PzXRhD9xAqigAmVCfSDOKA56ljepQDJg/view?usp=drive_link'>Click Here</a>",tag]
            return JsonResponse({'message': message, 'response': res})
        
        if tag =='tybsccss':
            res=["TyBscCS syllabus below <br> <a href='https://drive.google.com/file/d/1r-BmqZivvWQ-hBnRHC4QUAJAHACvNgAK/view?usp=drive_link'>Click Here</a>",tag]
            return JsonResponse({'message': message, 'response': res})

        if tag == "csfaculty":
            res=[get_staff("BSc CS"),tag]
            return JsonResponse({'message': message, 'response': res})
        
        if tag == "bscfaculty":
            res=[get_staff("Bsc"),tag]
            return JsonResponse({'message': message, 'response': res})
        
        if tag == "bcomfaculty":
            res=[get_staff("BCom"),tag]
            return JsonResponse({'message': message, 'response': res})
        
        if tag == "bafaculty":
            res=[get_staff("BA"),tag]
            return JsonResponse({'message': message, 'response': res})
        
        if tag == "numstudent":
            res=[get_count("users","students"),tag]
            return JsonResponse({'message': message, 'response': res})
        
        if tag == "numteacher":
            res=[get_count("staff","teachers"),tag]
            return JsonResponse({'message': message, 'response': res})
        

        arr_list = ["timetableall",
                   "bsccs","tybsccs","sybsccs","fybsccs",
                   "bsc","tybsc","sybsc","fybsc",
                   "bcom","tybcom","sybcom","fybcom",
                   "ba","tyba","syba","fyba"     
                   ]

        if tag in arr_list:
            faculty = (tag)
            if tag =="timetableall":
                faculty = ("fybsc","sybsc","tybsc",
                           "fybsccs","sybsccs","tybsccs",
                           "fybcom","sybcom","tybcom",
                           "fyba","syba","tyba")
                ret = timetable(faculty)
                res=[ret,tag]
                return JsonResponse({'message': message, 'response': res})
                
            if tag =="bsc":
                faculty = ("fybsc","sybsc","tybsc")
                ret = timetable(faculty)
                res=[ret,tag]
                return JsonResponse({'message': message, 'response': res})
            
            if tag == "bsccs":
                faculty=("fybsccs","sybsccs","tybsccs")
                ret = timetable(faculty)
                res=[ret,tag]
                return JsonResponse({'message': message, 'response': res})
            
            if tag == "bcom":
                faculty=("fybcom","sybcom","tybcom")
                ret = timetable(faculty)
                res=[ret,tag]
                return JsonResponse({'message': message, 'response': res})
            
            if tag == "ba":
                faculty=("fyba","syba","tyba")
                ret = timetable(faculty)
                res=[ret,tag]
                return JsonResponse({'message': message, 'response': res})

            faculty = (f"{tag}"," ")
            print(faculty)
            ret = timetable(faculty)
            res=[ret,tag]
            return JsonResponse({'message': message, 'response': res})

        return JsonResponse({'message': message, 'response': res})
    
        
    return render(request, 'index.html',data)

def reg(request):
    return render(request,"register.html")


def login(request):
    write_status("false")
    if request.method=="POST":
        
        res = request.POST

        user  = res.get("user")
        password = res.get("pass")
    
        if type(user)==str:


       
            print(user,password)
            result = verify(user,password)
            if result:
                nm = get_name(user)[0]
                print('nm',nm)
                write_file(nm)
                print("user name write successful")
                write_status("true")
                print(result)
                
            
                print("name:",name[0])
                return HttpResponseRedirect("chat")
            else:
                messages.success(request, 'Invalid Username or password') 
                return HttpResponseRedirect("login")
            
        
    return render(request,'loginindex.html')       
    
def register(request):
    if request.method=="POST":
        res=request.POST
        print("res",res)
        name = res.get("firstname")+" "+res.get("middlename")+" "+res.get("lastname")
        email = res.get("email")
        phone = res.get("phone")
        dob = res.get("dob")
        address = res.get("address")
        create_pass = res.get("crpass")
        confirm_pass = res.get("cnpass")
        gender= res.get("gender")
        if type(email)==str:
            print(name,email,phone,dob,address,create_pass,gender)
            if create_pass==confirm_pass:
                
                result = reg_user(name,email,phone,dob,address,create_pass,gender)
                return HttpResponseRedirect("login")
    return render(request,"regindex.html")

def res(request):
    res = get_res()
    return render(request,'result.html')

def new(request):
    return render(request,"index.html")

def launch(request):
    return HttpResponseRedirect("login")
def gallery(request):
    return render(request,"imagegallery.html")




def forgotPass(request):
    if request.method=="POST":
        email = request.POST.get("emailtxt")
        print(email)
        res = verify_email(email)
        print("res : ",res)
        if res==True:
            write_file(email)
            email_send(email,send_otp())
            return HttpResponseRedirect("otpverify")
        else:        
            return HttpResponseRedirect("forgot")
    return render(request,"forgot.html")

def otpv(request):
    
        
    return render(request,"otpverify.html")

def createP(request):
    if request.method=="POST":
        crpass = request.POST.get("crpass")
        cnpass = request.POST.get("cnpass")
        
        if crpass == cnpass:
            messages.success(request, 'Your password was updated successfully!') 
            
            return HttpResponseRedirect("login")
        
        else:
            messages.success(request, 'Your failed password was updated successfully!') 
            
    return render(request,"createPass.html")

def reset(request):
    context={
        'title':'Email Verification',
        'gateway':"emailverification",
        }
    if request.method=='POST':
        email = request.POST.get('emailtxt')
        print(email)
        res = verify_email(email)
        if res==True:
            write_file(email)
            email_send(email,send_otp())
            print('otp send successfully')
            context={
                'title':'OTP Verification',
                'gateway':"otpverify",
            }
            return render(request,'passwordreset.html',context)
        get_otp = request.POST.get('otp')
        local_otp = read_otp()
        print('get_otp : ',get_otp,' local_otp : ',local_otp)
        if get_otp == local_otp:
            print('otp match successful')
            context={
                'title':'Create Password',
                'gateway':"createpass",
            }
            return render(request,'passwordreset.html',context)
        create_pass = request.POST.get('crpass')
        confirm_pass = request.POST.get('cnpass')
        if create_pass == confirm_pass:
            print('password update successfully')
            res = change_pass(create_pass)
            print(res)
            if res ==True:
                print('password update successful')
                messages.success(request, 'Your password was updated successfully!')            
                return HttpResponseRedirect("login")
            else:
                return render(request,'passwordreset.html')

    return render(request,'passwordreset.html',context)