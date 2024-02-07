# Generated by Django 4.1.3 on 2022-11-11 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0023_delete_staff_payroll'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff_Payroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff', models.CharField(blank=True, max_length=50, null=True)),
                ('salary', models.IntegerField(blank=True, default=0, null=True)),
                ('vat', models.IntegerField(blank=True, default=0, null=True)),
                ('trustfund', models.IntegerField(blank=True, default=0, null=True)),
                ('r_sal', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
