# Generated by Django 2.2.1 on 2019-05-13 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titre')),
                ('subtitle', models.CharField(max_length=200, null=True, verbose_name='Sous-titre')),
                ('filtres', models.CharField(max_length=200, verbose_name='Filtres séparés par un espace')),
                ('link', models.CharField(max_length=200, verbose_name="Lien vers l'image ou la vidéo")),
                ('width', models.IntegerField(verbose_name='Largeur de la miniature dans le portfolio')),
                ('height', models.IntegerField(verbose_name='Hauteur de la miniature dans le portfolio')),
                ('column', models.IntegerField(verbose_name='Nombre de colonnes de la miniature dans le portfolio')),
                ('order', models.IntegerField(verbose_name="Ordre d'affichage")),
            ],
            options={
                'verbose_name': 'Média',
                'ordering': ['order'],
            },
        ),
    ]
