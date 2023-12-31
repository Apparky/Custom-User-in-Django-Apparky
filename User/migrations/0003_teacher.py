# Generated by Django 4.2.4 on 2023-08-24 15:39

import django.contrib.auth.models
from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):
    dependencies = [
        ("User", "0002_student"),
    ]

    operations = [
        migrations.CreateModel(
            name="Teacher",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("User.user",),
            managers=[
                ("teacher", django.db.models.manager.Manager()),
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
