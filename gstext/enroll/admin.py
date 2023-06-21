from django.contrib import admin

# Register your models here.
from .models import student

@admin.register(student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','student_name','student_roll']