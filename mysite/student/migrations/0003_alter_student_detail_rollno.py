# Generated by Django 4.1.4 on 2022-12-09 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_student_mark_chem_alter_student_mark_eng_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_detail',
            name='rollno',
            field=models.CharField(default='rollno', max_length=10, unique=True),
        ),
    ]
