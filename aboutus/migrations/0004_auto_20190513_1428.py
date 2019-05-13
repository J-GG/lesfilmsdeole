# Generated by Django 2.2.1 on 2019-05-13 12:28

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0003_auto_20190513_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutuscontent',
            name='heading',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Entête'),
        ),
        migrations.AlterField(
            model_name='aboutuscontent',
            name='more_content',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name="Contenu du bloc d'informations supplémentaires"),
        ),
        migrations.AlterField(
            model_name='aboutuscontent',
            name='more_title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name="Titre du bloc d'informations supplémentaires"),
        ),
    ]