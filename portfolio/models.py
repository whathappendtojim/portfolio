# portfolio/models.py
from django.db import models
from django.conf import settings

class PPTFile(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='ppt_files/')

    def __str__(self):
        return self.title

class ExcelFile(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='excel_files/')

    def __str__(self):
        return self.title

class PythonProject(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='python_files/')

    def __str__(self):
        return self.title
