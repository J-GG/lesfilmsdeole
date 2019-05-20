from django.db import models
from ckeditor.fields import RichTextField
from filer.fields.image import FilerImageField


class AboutUsContent(models.Model):
    """Content of the about us section."""

    title = models.CharField(max_length=200, verbose_name="Titre")
    heading = RichTextField(blank=True, null=True, verbose_name="Entête")
    text_before_more = RichTextField(blank=True, null=True,
                                     verbose_name="Texte avant le bloc d'informations supplémentaires")
    more_title = models.CharField(blank=True, null=True, max_length=200,
                                  verbose_name="Titre du bloc d'informations supplémentaires")
    more_content = RichTextField(blank=True, null=True, verbose_name="Contenu du bloc d'informations supplémentaires")

    text_after_more = RichTextField(blank=True, null=True,
                                    verbose_name="Texte après le bloc d'informations supplémentaires")

    class Meta:
        verbose_name = "Contenu"

    def __str__(self):
        return self.title


class AboutUsInfo(models.Model):
    """Represents an info to be displayed."""

    icon = FilerImageField(blank=True, null=True, verbose_name="Icône",
                           on_delete=models.SET_NULL, related_name="about_us_info_icon")
    title = models.CharField(blank=True, null=True, max_length=200, verbose_name="Titre")
    description = RichTextField(blank=True, null=True, verbose_name="Description")
    order = models.IntegerField(verbose_name="Ordre d'affichage")

    class Meta:
        verbose_name = "Point d'information"
        ordering = ["order"]

    def __str__(self):
        return self.title
