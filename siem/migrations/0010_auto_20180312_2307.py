# Generated by Django 2.0.1 on 2018-03-13 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siem', '0009_auto_20180222_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='limitrule',
            name='command_filter',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='logevent',
            name='command',
            field=models.CharField(default='', max_length=64),
        ),
    ]