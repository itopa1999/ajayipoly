# Generated by Django 4.1.3 on 2022-11-21 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0047_remove_status_bg'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='lecturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.lecturer'),
        ),
    ]