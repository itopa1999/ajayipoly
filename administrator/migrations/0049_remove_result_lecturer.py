# Generated by Django 4.1.3 on 2022-11-21 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0048_result_lecturer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='lecturer',
        ),
    ]
