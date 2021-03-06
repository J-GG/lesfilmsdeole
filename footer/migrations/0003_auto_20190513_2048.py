# Generated by Django 2.2.1 on 2019-05-13 18:48

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import filer.fields.file
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('footer', '0002_auto_20190513_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footercontent',
            name='background',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='background', to=settings.FILER_IMAGE_MODEL, verbose_name='Image de fond'),
        ),
        migrations.AlterField(
            model_name='footercontent',
            name='legal_notice',
            field=filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='legal_notice', to='filer.File', verbose_name='Mentions légales'),
        ),
        migrations.AlterField(
            model_name='footercontent',
            name='terms',
            field=filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='terms', to='filer.File', verbose_name='Conditions générales de ventes'),
        ),
    ]
