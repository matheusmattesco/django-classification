# Generated by Django 5.2 on 2025-04-08 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_iris', '0002_irismodel_asd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='irismodel',
            name='asd',
        ),
    ]
