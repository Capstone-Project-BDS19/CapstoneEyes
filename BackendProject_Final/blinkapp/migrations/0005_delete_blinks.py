# Generated by Django 4.0.4 on 2022-04-20 02:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blinkapp', '0004_remove_blinks_blink_count_remove_blinks_comp_dur_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='blinks',
        ),
    ]
