# Generated by Django 2.2.1 on 2020-01-03 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0010_auto_20200103_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactcontent',
            name='map',
            field=models.URLField(blank=True, max_length=400, null=True, verbose_name='Lien Google map'),
        ),
    ]
