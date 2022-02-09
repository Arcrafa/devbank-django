from django.contrib import admin
from .models import *
# Register your models here.

class InterestedAdmin(admin.ModelAdmin):
        list_display = ('full_name', 'student_code', 'email','category')

admin.site.register(Interested,InterestedAdmin)
