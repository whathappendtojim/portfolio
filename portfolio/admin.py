# portfolio/admin.py
from django.contrib import admin
from .models import PPTFile, ExcelFile, PythonProject

admin.site.register(PPTFile)
admin.site.register(ExcelFile)
admin.site.register(PythonProject)
