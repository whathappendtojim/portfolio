# portfolio/views.py
from django.shortcuts import render
from .models import PPTFile, ExcelFile, PythonProject

def home(request):
    return render(request, 'portfolio/home.html')

def ppt_files(request):
    files = PPTFile.objects.all()
    return render(request, 'portfolio/ppt_files.html', {'files': files})

def excel_files(request):
    files = ExcelFile.objects.all()
    return render(request, 'portfolio/excel_files.html', {'files': files})

def python_projects(request):
    projects = PythonProject.objects.all()
    return render(request, 'portfolio/python_projects.html', {'projects': projects})
