# Generated by Django 4.2.7 on 2023-11-07 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aggregates', '0007_add_user_list_flags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linkaggregate',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='pageprojectaggregate',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='useraggregate',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
