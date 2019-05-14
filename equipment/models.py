from django.db import models
from filer.fields.image import FilerImageField
from ckeditor.fields import RichTextField


class EquipmentContent(models.Model):
    """Content of the equipment section."""

    title = models.CharField(max_length=200, verbose_name="Titre")
    heading = RichTextField(blank=True, null=True, verbose_name="Entête")
    text_before_list = RichTextField(blank=True, null=True, verbose_name="Texte avant la liste")

    class Meta:
        verbose_name = "Contenu"

    def __str__(self):
        return self.title


class Equipment(models.Model):
    """Represents an equipment to be displayed."""

    name = models.CharField(max_length=100, verbose_name="Nom")
    image = FilerImageField(blank=True, null=True, verbose_name="Image", on_delete=models.SET_NULL)
    description = RichTextField(blank=True, null=True, verbose_name="Description")
    order = models.IntegerField(verbose_name="Ordre d'affichage")

    class Meta:
        verbose_name = "Equipement"
        ordering = ["order"]

    def __str__(self):
        return self.name
