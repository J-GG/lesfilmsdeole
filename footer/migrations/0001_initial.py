# Generated by Django 2.2.1 on 2019-05-13 17:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.file
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('filer', '0011_auto_20190418_0137'),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200, verbose_name='Texte')),
                ('background', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='background', to=settings.FILER_IMAGE_MODEL, verbose_name='Image de fond')),
                ('legal_notice', filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='legal_notice', to='filer.File', verbose_name='Mentions légales')),
                ('terms', filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='terms', to='filer.File', verbose_name='Conditions générales de ventes')),
            ],
            options={
                'verbose_name': 'Contenu',
            },
        ),
    ]