# Generated by Django 2.2.1 on 2019-05-12 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('industries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titre')),
                ('heading', models.TextField(verbose_name='Entête')),
            ],
        ),
        migrations.AlterField(
            model_name='industry',
            name='description',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='industry',
            name='icon',
            field=models.CharField(max_length=50, null=True, verbose_name='Icône'),
        ),
        migrations.AlterField(
            model_name='industry',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='industry',
            name='order',
            field=models.IntegerField(verbose_name="Ordre d'affichage"),
        ),
    ]