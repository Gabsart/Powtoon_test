# Generated by Django 4.0.3 on 2022-04-09 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('powtoon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='powtoon',
            name='contentJson',
            field=models.JSONField(default='dict'),
        ),
    ]
