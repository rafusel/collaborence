# Generated by Django 3.0.2 on 2020-01-26 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20200125_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='term',
            field=models.CharField(default='Winter', max_length=10),
        ),
        migrations.AddField(
            model_name='course',
            name='year',
            field=models.IntegerField(default=2020),
        ),
    ]
