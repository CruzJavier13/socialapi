# Generated by Django 5.0.2 on 2024-04-12 20:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentpost',
            name='user',
        ),
        migrations.AddField(
            model_name='commentpost',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.user'),
            preserve_default=False,
        ),
    ]
