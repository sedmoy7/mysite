# Generated by Django 4.2.4 on 2023-08-22 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='author',
        ),
    ]
