# Generated by Django 5.1.6 on 2025-03-28 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_admin', '0002_remove_alladmin_state_alladmin_city_alladmin_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alladmin',
            name='mail',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email'),
        ),
    ]
