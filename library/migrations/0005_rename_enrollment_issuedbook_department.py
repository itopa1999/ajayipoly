# Generated by Django 3.2.4 on 2022-10-28 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20221027_2039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issuedbook',
            old_name='enrollment',
            new_name='department',
        ),
    ]
