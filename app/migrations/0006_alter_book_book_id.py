# Generated by Django 3.2.2 on 2022-04-08 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_book_book_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_id',
            field=models.CharField(max_length=20),
        ),
    ]
