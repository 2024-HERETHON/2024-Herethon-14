# Generated by Django 5.0.6 on 2024-07-03 14:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcomment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poem.poempost'),
        ),
    ]
