from django.contrib import admin

# Register your models here.
from .models import MyModel

@admin.register(MyModel)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','field1','field2']