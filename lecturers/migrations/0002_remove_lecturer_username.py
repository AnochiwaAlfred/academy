# Generated by Django 4.1.1 on 2023-01-19 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lecturers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecturer',
            name='username',
        ),
    ]
