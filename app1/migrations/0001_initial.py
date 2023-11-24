# Generated by Django 2.2.4 on 2023-11-23 18:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('network', models.CharField(max_length=45)),
                ('releasedate', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('description', models.TextField()),
                ('creates_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
