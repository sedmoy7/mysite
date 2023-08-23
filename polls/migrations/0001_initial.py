# Generated by Django 4.2.4 on 2023-08-23 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=255)),
                ('option_one', models.CharField(max_length=50)),
                ('option_two', models.CharField(max_length=50)),
                ('option_three', models.CharField(max_length=50)),
                ('option_one_count', models.IntegerField(default=0)),
                ('option_two_count', models.IntegerField(default=0)),
                ('option_three_count', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
            ],
        ),
    ]
