# Generated by Django 4.1 on 2023-07-21 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("drfdemo", "0002_alter_student_class_null"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="age",
            field=models.IntegerField(null=True, verbose_name="年龄"),
        ),
        migrations.AlterField(
            model_name="student",
            name="class_null",
            field=models.CharField(max_length=5, null=True, verbose_name="班级编号"),
        ),
        migrations.AlterField(
            model_name="student",
            name="sex",
            field=models.BooleanField(default=1, verbose_name="性别"),
        ),
    ]