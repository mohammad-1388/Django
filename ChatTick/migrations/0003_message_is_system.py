# Generated by Django 3.1.7 on 2021-04-01 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChatTick', '0002_group_messagegroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='is_system',
            field=models.BooleanField(default=False, verbose_name='از طرف سیستم'),
        ),
    ]
