# Generated by Django 2.2 on 2019-04-29 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0004_auto_20190426_1245'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='linkevent',
            options={'get_latest_by': 'timestamp'},
        ),
    ]
