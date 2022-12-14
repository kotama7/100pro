from django.contrib import admin

# Register your models here.
from .models import Schedule,Individual_data

admin.site.register(Schedule)
admin.site.register(Individual_data)