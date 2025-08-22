from django.shortcuts import render,redirect
from .models import Contact,SportCourse,Feedback,User,Coach,Notice
from django.contrib import messages

# Create your views here.
def home(request):
    notice_list=Notice.objects.all()






    feedback=Feedback.objects.all()
    data=[]
    # User.name
    for f in feedback:
       data.append(
          {
             "rating":f.rating,
             "remarks":f.remarks,
             "name":f.name,
             "profile_pic":User.objects.filter(email=f.email)[0].profile_pic

          }
       )
    Feedback_dict={
         "feedback_key":data,
         "notice_key":notice_list

      }
    return render(request,'sport_app/html/index.html',Feedback_dict)

def contact(request):
    if request.method=="GET":
     return render(request,'sport_app/html/contact_us.html')
    if request.method=="POST":
       user_name= request.POST["name"]
       user_email= request.POST["email"]
       user_query= request.POST["query"]
       user_phone= request.POST["phone"]
       

       #fetch value from all text field
       #create object of contact model and save
       contact_obj=Contact(name=user_name,email=user_email,phone=user_phone,query=user_query)
       contact_obj.save()
       messages.success(request,"We'll Reach You Soon👍🏻")

       return redirect("contact")

def about(request):
    return render(request,'sport_app/html/about_us.html')

def about_academy(request):
    return render(request,'sport_app/html/about_academy.html')


def cricket(request):
    return render(request,'sport_app/html/cricket.html')

def basketball(request):
    return render(request,'sport_app/html/basketball.html')


def badminton(request):
    return render(request,'sport_app/html/badminton.html')

def football(request):
    return render(request,'sport_app/html/football.html')



def view_programs(request):
   course_list=SportCourse.objects.all() #select * from SportCourse
   context={
      "course_key":course_list
   }


   return render(request,"sport_app/html/view_programs.html",context)

def coach(request):
     coach_list=Coach.objects.all() #select * from SportCourse
     coach_dict={
      "coach_key":coach_list

   }
     return render(request,'sport_app/html/coach.html',coach_dict)
