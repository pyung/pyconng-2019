# Generated by Django 2.2.3 on 2019-07-31 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0006_auto_20190705_2215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proposal',
            name='profile_picture',
        ),
    ]
