# Generated by Django 4.2.13 on 2024-07-10 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="excelfile",
            name="file",
            field=models.FileField(upload_to="D:\\My_Site\\excel_files"),
        ),
        migrations.AlterField(
            model_name="pptfile",
            name="file",
            field=models.FileField(upload_to="D:\\My_Site\\ppt_files"),
        ),
        migrations.AlterField(
            model_name="pythonproject",
            name="file",
            field=models.FileField(upload_to="D:\\My_Site\\python_files"),
        ),
    ]
