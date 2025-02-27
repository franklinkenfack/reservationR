# Generated by Django 5.1.6 on 2025-02-24 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityCrossLine',
            fields=[
                ('city_id', models.AutoField(primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=100)),
                ('city_name', models.CharField(max_length=100)),
                ('line', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'CityCross',
                'verbose_name_plural': 'CitiesCross',
            },
        ),
    ]
