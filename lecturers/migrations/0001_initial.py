# Generated by Django 4.1.1 on 2023-01-02 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departments', '0001_initial'),
        ('faculties', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('idNumber', models.CharField(max_length=15, unique=True)),
                ('firstName', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=200)),
                ('dateOfBirth', models.DateField()),
                ('title', models.CharField(choices=[('Mr.', 'Mr.'), ('Mrs.', 'Mrs.'), ('Miss.', 'Miss.'), ('Dr.', 'Dr.'), ('Engr.', 'Engr.'), ('Barr.', 'Barr.'), ('Prof.', 'Prof.')], max_length=5)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('rank', models.CharField(choices=[('Lecturer Assistant', 'Lecturer Assistant'), ('Assistant Lecturer', 'Assistant Lecturer'), ('Lecturer I', 'Lecturer I'), ('Lecturer II', 'Lecturer II'), ('Senior Lecturer', 'Senior Lecturer'), ('Associate Professor', 'Associate Professor'), ('Professor', 'Professor')], max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('address', models.TextField()),
                ('yearOfAppointment', models.DateField()),
                ('username', models.EmailField(max_length=100, unique=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.department')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculties.faculty')),
            ],
        ),
    ]