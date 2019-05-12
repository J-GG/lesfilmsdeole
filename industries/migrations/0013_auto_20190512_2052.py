# Generated by Django 2.2.1 on 2019-05-12 18:52

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('industries', '0012_auto_20190512_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='industriescontent',
            name='heading',
            field=ckeditor.fields.RichTextField(default='test', verbose_name='Entête'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='industriescontent',
            name='title',
            field=models.CharField(default='test', max_length=200, verbose_name='Titre'),
            preserve_default=False,
        ),
    ]
