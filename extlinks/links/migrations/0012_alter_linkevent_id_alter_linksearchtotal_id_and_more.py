# Generated by Django 4.2.7 on 2023-11-07 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0011_auto_20230217_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linkevent',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='linksearchtotal',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='urlpattern',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
