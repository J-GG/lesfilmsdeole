# Generated by Django 2.2.1 on 2019-05-12 17:09

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('industries', '0011_auto_20190512_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='industriescontent',
            name='heading',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Entête'),
        ),
    ]