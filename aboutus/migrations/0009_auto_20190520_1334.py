# Generated by Django 2.2.1 on 2019-05-20 11:34

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0008_aboutusinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutuscontent',
            name='first_item_description',
        ),
        migrations.RemoveField(
            model_name='aboutuscontent',
            name='first_item_image',
        ),
        migrations.RemoveField(
            model_name='aboutuscontent',
            name='first_item_title',
        ),
        migrations.RemoveField(
            model_name='aboutuscontent',
            name='second_item_description',
        ),
        migrations.RemoveField(
            model_name='aboutuscontent',
            name='second_item_image',
        ),
        migrations.RemoveField(
            model_name='aboutuscontent',
            name='second_item_title',
        ),
        migrations.RemoveField(
            model_name='aboutuscontent',
            name='third_item_description',
        ),
        migrations.RemoveField(
            model_name='aboutuscontent',
            name='third_item_image',
        ),
        migrations.RemoveField(
            model_name='aboutuscontent',
            name='third_item_title',
        ),
        migrations.AlterField(
            model_name='aboutusinfo',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Description'),
        ),
    ]