# Generated by Django 4.0.4 on 2022-05-03 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blinkapp', '0017_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blnk',
            name='blink_cnt',
        ),
    ]
