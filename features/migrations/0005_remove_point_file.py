# Generated by Django 5.0.6 on 2024-06-17 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0004_alter_point_options_alter_point_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='point',
            name='file',
        ),
    ]