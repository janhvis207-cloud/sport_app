from django.shortcuts import render,redirect
from.models import User,Feedback,SportCourse,AdmissionForm,Coach
from django.contrib import messages



def user_coach(request):
   coach_list=Coach.objects.all()
   coach_dict={
      "coach_key":coach_list

   }

   return render(request,"sport_app/user/user_coach.html",coach_dict)



def user_logout(request):
   request.session.flush()
   messages.success(request,"Successfully logged out !!")
   return redirect("login")

def home (request):
   if request.method=="GET":
      user_email=request.session["web_key"]
      user_obj=User.objects.get(email=user_email)
      user_dict={"user_key":user_obj }

      return render(request,"sport_app/user/user_home.html",user_dict)


def user_login(request):
    if request.method=="GET":
     return render(request,"sport_app/user/user_login.html")
    if request.method=="POST":
       user_email=request.POST["email"]
       user_password=request.POST["password"]
       
    user_list= User.objects.filter(email=user_email,password=user_password)
    if len(user_list)>0:
       request.session["web_key"]=user_email ##binding email in a session to track user for multiple requests

       return redirect("home")
    else:
       messages.error(request,"invalid credentials")
       return redirect("login")


def feedback(request):
    if request.method=="GET":
     return render(request,'sport_app/user/user_feedback.html')
    
    if request.method=="POST":
       user_name= request.POST["name"]  #control name input field#
       user_email=request.session["web_key"]
       user_remarks=request.POST["remarks"]
       user_rating=request.POST["rating"]

       ##ORMAPPING FRAMEWORK##

       ## create object of user models
       ##set values
       ##save object -> it automatically sotres values in tables

       feedback_obj=Feedback(name=user_name,email=user_email,remarks=user_remarks,rating=user_rating)
       feedback_obj.save()

       messages.success(request,"THANK YOU FOR YOUR TIME")

       return redirect("feedback")
    
    def coach(request):
     coach_list=Coach.objects.all() #select * from SportCourse
     coach_dict={
      "coach_key":coach_list

   }
     return render(request,'sport_app/user/user_coach.html',coach_dict)


       

def registration(request):
    if request.method=="GET":
      return render(request,"sport_app/user/user_registration.html")
    
    if request.method=="POST":
       user_email= request.POST["email"]  #control name input field#
       user_password=request.POST["password"]
       user_name=request.POST["name"]
       user_phone=request.POST["phone"]
       user_pic=request.FILES["profile_pic"]

       ##ORMAPPING FRAMEWORK##

       ## create object of user models
       ##set values
       ##save object -> it automatically sotres values in tables

       user_obj=User(name=user_name,email=user_email,password=user_password,phone=user_phone,profile_pic=user_pic)
       user_obj.save()
       return redirect("login")
    
def user_editprofile(request):
       if request.method=="GET":
          user_email=request.session["web_key"]
          user_obj=User.objects.get(email=user_email)
          user_dict={
             "user_key":user_obj
          }

          return render(request,"sport_app/user/user_editprofile.html",user_dict)
       if request.method=="POST":
          user_name=request.POST["name"]
          user_phone=request.POST["phone"]
          user_pic=request.FILES.get("pic")
          user_email=request.session["web_key"]
          user_obj=User.objects.get(email=user_email)
          if user_pic is not None:
             user_obj.profile_pic=user_pic
          user_obj.name=user_name
          user_obj.phone=user_phone
          user_obj.save()
          messages.success(request,"Profile Updated")
          return redirect("user_home")
       
    
def admission_status(request):
          if request.method=="GET":
             email=request.session["web_key"]
             form_obj=AdmissionForm.objects.get(user_email=email)
             form_dict={
                
                "form_key":form_obj
             
             }
             return render(request,"sport_app/user/admission_status.html",form_dict)

def admission(request):
     if request.method=="GET":
      user_email=request.session["web_key"]

   
      course_list=SportCourse.objects.all()
      course_dict={
            "course_key":course_list,
            "email":user_email
         }

      return render(request,'sport_app/user/admission_form.html',course_dict)
     
     if request.method=="POST":
        
       course_name= request.POST["course_name"]  #control name input field#
       user_email=request.POST["email"]
       user_name=request.POST["name"]
       user_dob=request.POST["DOB"]
       user_phone=request.POST["phone"]
       user_gender=request.POST["gender"]
       user_address=request.POST["address"]
       user_pic=request.FILES["admission_pic"]

       admission_obj=AdmissionForm(course_name=course_name,user_email=user_email,full_name=user_name,date_of_birth=user_dob,phone=user_phone,gender=user_gender,address=user_address,pic_name=user_pic)
       admission_obj.save()
       return redirect("admission_form")

    