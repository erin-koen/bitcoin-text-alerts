# Generated by Django 2.2.5 on 2019-09-13 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='alert_count',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
