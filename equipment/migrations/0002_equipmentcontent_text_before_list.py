# Generated by Django 2.2.1 on 2019-05-14 15:21

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipmentcontent',
            name='text_before_list',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Texte avant la liste'),
        ),
    ]
