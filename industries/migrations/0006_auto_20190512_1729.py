# Generated by Django 2.2.1 on 2019-05-12 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('industries', '0005_auto_20190512_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='industriescontent',
            name='background',
            field=models.ImageField(blank=True, null=True, upload_to='industries/', verbose_name='Image de fond'),
        ),
    ]