# Generated by Django 4.1.1 on 2023-01-02 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('faculties', '0001_initial'),
        ('departments', '0001_initial'),
        ('levels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('courseCode', models.CharField(max_length=7, unique=True)),
                ('courseTitle', models.CharField(max_length=100)),
                ('creditLoad', models.IntegerField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.department')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculties.faculty')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='levels.level')),
            ],
        ),
    ]