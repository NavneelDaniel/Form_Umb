# Generated by Django 2.0.7 on 2019-07-14 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0003_auto_20190713_0044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='Flatno',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='address',
        ),
    ]
