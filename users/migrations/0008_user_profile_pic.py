# Generated by Django 4.1.3 on 2022-11-06 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20221024_0321'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profilepic.png', null=True, upload_to=''),
        ),
    ]
