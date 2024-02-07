# Generated by Django 4.1.3 on 2022-11-11 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0027_alter_staff_payroll_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='bg',
            field=models.CharField(choices=[('success', '1'), ('Option2', 'Option2'), ('Option3', 'Option3'), ('Option4', 'Option4')], default='success', max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='status',
            name='expiry',
            field=models.DateField(blank=True, null=True),
        ),
    ]
