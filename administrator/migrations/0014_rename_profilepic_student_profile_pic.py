# Generated by Django 3.2.4 on 2022-10-30 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0013_student_profilepic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='profilepic',
            new_name='profile_pic',
        ),
    ]