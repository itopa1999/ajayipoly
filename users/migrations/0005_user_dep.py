# Generated by Django 3.2.4 on 2022-10-24 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_department_faculty'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dep',
            field=models.CharField(max_length=20, null=True),
        ),
    ]