from django.contrib import admin
from . models import *

class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id','name','answer','question']
    list_filter = ['name','question']

admin.site.register(Questions)
admin.site.register(Answer,AnswerAdmin)
