# Generated by Django 3.2.6 on 2021-08-21 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('1', 'Male'), ('2', 'Female'), ('3', 'Other'), ('4', 'Prefer not to say')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='avatar_04.png', null=True, upload_to=''),
        ),
    ]