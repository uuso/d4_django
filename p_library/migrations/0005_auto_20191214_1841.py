# Generated by Django 2.2.6 on 2019-12-14 18:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0004_auto_20191207_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='in_stock',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='lease',
            name='date_back',
            field=models.DateField(default=datetime.date(2019, 12, 28)),
        ),
    ]
