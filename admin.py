from django.contrib import admin
from.models import Contact,Feedback,User,SportCourse,Coach,Notice,AdmissionForm

class Contact_Admin(admin.ModelAdmin):
    list_display=["name","email","query","phone","date"]
    
class Feedback_Admin(admin.ModelAdmin):
    list_display=["name","email","remarks","rating","date"]
    



admin.site.register(Contact,Contact_Admin)
admin.site.register(Feedback,Feedback_Admin)
admin.site.register(User)
admin.site.register(SportCourse)
admin.site.register(Coach)
admin.site.register(AdmissionForm)
admin.site.register(Notice)


admin.site.site_header="Sport Admin Dashboard"
admin.site.site_title="SpreadThe Joy Of Playing"
admin.site.index_title="Sport Academy"
