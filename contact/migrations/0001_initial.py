# Generated by Django 2.2.1 on 2019-05-14 13:05

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
            name='ContactContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titre')),
                ('heading', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Entête')),
                ('address', models.CharField(max_length=200, verbose_name='Adresse')),
                ('phone', models.CharField(max_length=200, verbose_name='Téléphone')),
                ('email', models.EmailField(max_length=200, verbose_name='Adresse email')),
                ('facebook_plugin', models.URLField(verbose_name='Lien plugin FB')),
                ('facebook', models.URLField(verbose_name='Lien FB')),
                ('youtube', models.URLField(verbose_name='Lien Youtube')),
                ('vimeo', models.URLField(verbose_name='Lien Viméo')),
                ('background', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contact_background', to=settings.FILER_IMAGE_MODEL, verbose_name='Image de fond')),
            ],
        ),
    ]
