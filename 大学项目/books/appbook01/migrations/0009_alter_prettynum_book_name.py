# Generated by Django 4.1 on 2023-08-11 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appbook01', '0008_alter_prettynum_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prettynum',
            name='book_name',
            field=models.CharField(default=0, max_length=300, verbose_name='书名'),
        ),
    ]
