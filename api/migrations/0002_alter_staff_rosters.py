# Generated by Django 4.1 on 2023-04-17 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='rosters',
            field=models.ManyToManyField(blank=True, to='api.roster'),
        ),
    ]
