from django.contrib import admin

# Register your models here.
from .models import Organizer,Feedback,Program_details,Job_description,Cityevents,Contactus
admin.site.register(Organizer)
admin.site.register(Feedback)
admin.site.register(Program_details)
admin.site.register(Job_description)
admin.site.register(Cityevents)
admin.site.register(Contactus)