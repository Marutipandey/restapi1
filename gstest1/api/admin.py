from django.contrib import admin
from .models import rewardss
# Register your models here.
@admin.register(rewardss)
class rewardAdmin(admin.ModelAdmin):
    list_display =['id','amount']