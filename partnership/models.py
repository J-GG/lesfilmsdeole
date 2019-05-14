from django.db import models
from ckeditor.fields import RichTextField
from filer.fields.image import FilerImageField


class PartnershipContent(models.Model):
    """Content of the partnership section."""

    title = models.CharField(max_length=200, verbose_name="Titre")
    heading = RichTextField(blank=True, null=True, verbose_name="Entête")

    class Meta:
        verbose_name = "Contenu"

    def __str__(self):
        return self.title


class Partner(models.Model):
    """Represents an industry to be displayed."""

    name = models.CharField(max_length=100, verbose_name="Nom du partenaire")
    link = models.URLField(max_length=50, blank=True, null=True, verbose_name="Lien du partenaire")
    logo = FilerImageField(verbose_name="Logo du partenaire", blank=True, null=True, on_delete=models.SET_NULL,
                           related_name="partner_logo")
    order = models.IntegerField(verbose_name="Ordre d'affichage")

    class Meta:
        verbose_name = "Partenaire"
        ordering = ["order"]

    def __str__(self):
        return self.name
