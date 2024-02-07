# Generated by Django 4.1.3 on 2022-11-19 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0040_alter_status_expiry'),
    ]

    operations = [
        migrations.AddField(
            model_name='departmentnotice',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='departmentnotice',
            name='level',
            field=models.CharField(blank=True, choices=[('ND', 'ND'), ('HND', 'HND')], default='ND', max_length=200, null=True),
        ),
    ]
