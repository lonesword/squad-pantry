# Generated by Django 2.0 on 2018-02-06 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squad_pantry_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configurationsettings',
            name='value',
            field=models.CharField(max_length=256),
        ),
    ]
