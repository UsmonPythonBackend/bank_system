# Generated by Django 5.1 on 2024-08-16 13:04

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('course_id', models.PositiveIntegerField()),
                ('student_id', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('PROCESSING', 'Processing'), ('REJECTED', 'Rejecting'), ('CANCELED', 'Canceled'), ('SUCCEEDED', 'Succeeded')], default='PENDING', max_length=15)),
                ('publish', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
