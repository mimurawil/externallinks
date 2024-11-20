# Generated by Django 4.2.14 on 2024-09-27 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('organisations', '0008_alter_collection_id_alter_organisation_id_and_more'),
        ('links', '0012_alter_linkevent_id_alter_linksearchtotal_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='linkevent',
            name='content_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='content_type', to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='linkevent',
            name='object_id',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='urlpattern',
            name='collections',
            field=models.ManyToManyField(related_name='urlpatterns', to='organisations.collection'),
        ),
        migrations.AddIndex(
            model_name='linkevent',
            index=models.Index(fields=['content_type', 'object_id'], name='links_linke_content_1a162a_idx'),
        ),
    ]
