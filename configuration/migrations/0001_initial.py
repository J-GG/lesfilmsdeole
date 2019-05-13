# Generated by Django 2.2.1 on 2019-05-13 12:59

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titre du site')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Description du site (apparait dans les moteurs de cherche)')),
                ('favicon', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.FILER_IMAGE_MODEL, verbose_name='Icône dans le navigateur')),
            ],
            options={
                'verbose_name': 'Configuration',
            },
        ),
    ]
