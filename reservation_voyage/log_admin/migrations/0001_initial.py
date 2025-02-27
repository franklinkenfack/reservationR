# Generated by Django 5.1.6 on 2025-02-24 19:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('all_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogAdmin',
            fields=[
                ('log_id', models.AutoField(primary_key=True, serialize=False)),
                ('all_admin_some_id', models.CharField(blank=True, max_length=100, null=True)),
                ('driver_id', models.CharField(blank=True, max_length=100, null=True)),
                ('vehicle_id', models.CharField(blank=True, max_length=100, null=True)),
                ('agency_id', models.CharField(blank=True, max_length=100, null=True)),
                ('trip_id', models.CharField(blank=True, max_length=100, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('all_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='all_admin.alladmin')),
            ],
            options={
                'verbose_name': 'LogAdmin',
                'verbose_name_plural': 'LogAdmins',
            },
        ),
    ]
