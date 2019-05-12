# Generated by Django 2.2.1 on 2019-05-12 14:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('industries', '0004_auto_20190512_1610'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='industriescontent',
            options={'verbose_name': 'Contenu'},
        ),
        migrations.AddField(
            model_name='industriescontent',
            name='background',
            field=models.FileField(default=django.utils.timezone.now, upload_to='', verbose_name='Image de fond'),
            preserve_default=False,
        ),
    ]
