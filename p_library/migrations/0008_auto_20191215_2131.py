# Generated by Django 2.2.6 on 2019-12-15 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0007_auto_20191215_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='photo',
            field=models.ImageField(default='images/no-image.jpg', upload_to='images/'),
        ),
    ]
