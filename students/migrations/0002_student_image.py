# Generated by Django 4.1.1 on 2023-01-24 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(default='', upload_to='media'),
            preserve_default=False,
        ),
    ]
