# Generated by Django 4.1 on 2023-07-21 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("drfdemo", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="class_null",
            field=models.CharField(max_length=5, verbose_name="班级编号"),
        ),
    ]
