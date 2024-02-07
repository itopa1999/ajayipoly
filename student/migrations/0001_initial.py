# Generated by Django 3.2.4 on 2022-10-24 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0004_department_faculty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_id', models.CharField(blank=True, max_length=12)),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.department')),
            ],
        ),
    ]
