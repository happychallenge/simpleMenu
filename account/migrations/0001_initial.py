# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-21 09:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthdate', models.DateTimeField(blank=True, null=True, verbose_name='Birth Date')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='person_profile/%Y/%m/', verbose_name='Profile Picture')),
                ('num', models.IntegerField(blank=True, null=True, verbose_name='UID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('friends', models.ManyToManyField(related_name='_profile_friends_+', to='account.Profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
