# Generated by Django 5.1.6 on 2025-02-24 08:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agence', '0001_initial'),
        ('superadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SysAdmin',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('admin_name', models.CharField(max_length=100)),
                ('Tel_number', models.CharField(max_length=15)),
                ('mail', models.EmailField(max_length=254)),
                ('authorised_agencies', models.ManyToManyField(related_name='admins', to='agence.agency')),
                ('super_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superadmin.superadmin')),
            ],
            options={
                'verbose_name': 'SysAdmin',
                'verbose_name_plural': 'SysAdmins',
            },
        ),
    ]
