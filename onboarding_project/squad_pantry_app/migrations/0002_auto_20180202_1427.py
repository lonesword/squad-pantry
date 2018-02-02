# Generated by Django 2.0 on 2018-02-02 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squad_pantry_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='is_available',
            field=models.BooleanField(default=False, help_text='Check if the dish is available'),
        ),
        migrations.AlterField(
            model_name='order',
            name='scheduled_time',
            field=models.DateTimeField(blank=True, help_text='Schedule Your Order. Leave it blank for getting your order as soon as possible', null=True),
        ),
    ]