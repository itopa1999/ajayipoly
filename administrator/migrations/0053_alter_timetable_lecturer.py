# Generated by Django 4.1.3 on 2022-11-23 00:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0052_timetable_lecturer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='lecturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.lecturer'),
        ),
    ]
