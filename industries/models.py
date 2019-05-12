from django.db import models


class IndustriesContent(models.Model):
    """Content of the industries section."""

    title = models.CharField(max_length=200, verbose_name="Titre")
    heading = models.TextField(verbose_name="Entête")
    background = models.ImageField(upload_to="industries/", blank=True, null=True, verbose_name="Image de fond")

    class Meta:
        verbose_name = "Contenu"

    def __str__(self):
        return self.title


class Industry(models.Model):
    """Represents an industry to be displayed."""

    name = models.CharField(max_length=100, verbose_name="Nom")
    icon = models.CharField(max_length=50, null=True, verbose_name="Icône")
    description = models.TextField(null=True, verbose_name="Description")
    order = models.IntegerField(verbose_name="Ordre d'affichage")

    class Meta:
        verbose_name = "Secteur d'activité"
        ordering = ["order"]

    def __str__(self):
        return self.name
