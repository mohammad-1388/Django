# Generated by Django 3.1.7 on 2021-03-31 21:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_auto_20210331_1304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='متن')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile', verbose_name='گیرنده')),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='نویسنده')),
            ],
            options={
                'verbose_name': 'پیام',
                'verbose_name_plural': 'پیام',
            },
        ),
    ]