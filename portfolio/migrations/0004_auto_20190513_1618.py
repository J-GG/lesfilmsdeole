# Generated by Django 2.2.1 on 2019-05-13 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20190513_1603'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfoliomedia',
            old_name='column',
            new_name='columns',
        ),
    ]
