# Generated by Django 2.2.6 on 2019-12-07 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0003_auto_20191207_1842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='copy_count',
        ),
        migrations.AddField(
            model_name='friend',
            name='is_library',
            field=models.BooleanField(default=False),
        ),
    ]
