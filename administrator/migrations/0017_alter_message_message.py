# Generated by Django 3.2.4 on 2022-10-30 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0016_auto_20221030_0517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(blank=True, max_length=3000),
        ),
    ]