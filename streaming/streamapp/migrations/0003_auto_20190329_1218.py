# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-29 12:18
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('streamapp', '0002_pointresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('blog_id', models.AutoField(primary_key=True, serialize=False)),
                ('blog_content', models.TextField()),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('last_edited', models.DateTimeField(default=datetime.datetime.now)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('is_approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('last_edited', models.DateTimeField(default=datetime.datetime.now)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='streamapp.Blog')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='streamapp.BlogCategory'),
        ),
    ]
