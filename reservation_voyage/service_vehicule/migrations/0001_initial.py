# Generated by Django 5.1.6 on 2025-02-24 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceAvailable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wifi', models.BooleanField(default=False)),
                ('electric_socket', models.BooleanField(default=False)),
                ('air_conditioning', models.BooleanField(default=False)),
                ('toilet', models.BooleanField(default=False)),
                ('seatbelt', models.BooleanField(default=False)),
                ('entertainment_screen', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'ServiceAvailable',
                'verbose_name_plural': 'ServicesAvailable',
            },
        ),
    ]
