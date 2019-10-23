# Generated by Django 2.2.1 on 2019-07-29 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20190521_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactcontent',
            name='email_footer',
            field=models.CharField(default="Message envoyé via le formulaire de contact des Films d'Éole.", max_length=250, verbose_name='Message affiché en bas de chaque email reçu.'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactcontent',
            name='email_subject',
            field=models.CharField(default='', max_length=250, verbose_name="Sujet de l'email précédant le sujet rempli dans le formulaire du contact."),
            preserve_default=False,
        ),
    ]