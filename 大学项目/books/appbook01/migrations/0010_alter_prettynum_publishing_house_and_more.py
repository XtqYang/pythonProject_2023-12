# Generated by Django 4.1 on 2023-08-11 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appbook01', '0009_alter_prettynum_book_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prettynum',
            name='Publishing_house',
            field=models.CharField(default=0, max_length=300, verbose_name='出版社'),
        ),
        migrations.AlterField(
            model_name='prettynum',
            name='author',
            field=models.CharField(default=0, max_length=200, verbose_name='作者'),
        ),
    ]
