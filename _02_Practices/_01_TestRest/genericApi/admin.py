from django.contrib import admin
from .models import studentsInfo

# Register your models here.
@admin.register(studentsInfo)
class registerUser(admin.ModelAdmin):
    list_display = ['id','name', 'city', 'roll_no', 'is_active']
