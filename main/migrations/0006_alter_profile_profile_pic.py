# Generated by Django 3.2.6 on 2021-08-22 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210821_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='avatar_03.png', null=True, upload_to=''),
        ),
    ]
