# Generated by Django 3.2 on 2021-04-28 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_visit', '0002_alter_book_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='student',
        ),
        migrations.AddField(
            model_name='book',
            name='email',
            field=models.CharField(default='', max_length=50),
        ),
    ]
