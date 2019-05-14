from django.db import models
from filer.fields.image import FilerImageField
from ckeditor.fields import RichTextField


class PricingContent(models.Model):
    """Content of the pricing section."""

    title = models.CharField(max_length=200, verbose_name="Titre")
    heading = RichTextField(blank=True, null=True, verbose_name="Entête")
    background = FilerImageField(blank=True, null=True, verbose_name="Image de fond",
                                 on_delete=models.SET_NULL, related_name="pricing_background")

    class Meta:
        verbose_name = "Contenu"

    def __str__(self):
        return self.title


class Price(models.Model):
    """Represents a price to be displayed."""

    name = models.CharField(max_length=100, verbose_name="Nom")
    subtitle = models.CharField(blank=True, null=True, max_length=250, verbose_name="Sous-titre")
    description = RichTextField(blank=True, null=True, verbose_name="Description")
    order = models.IntegerField(verbose_name="Ordre d'affichage")

    class Meta:
        verbose_name = "Prestation"
        ordering = ["order"]

    def __str__(self):
        return self.name
