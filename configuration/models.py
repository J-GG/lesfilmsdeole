from django.db import models
from ckeditor.fields import RichTextField
from filer.fields.image import FilerImageField


class Configuration(models.Model):
    """Configuration of the website."""

    title = models.CharField(max_length=200, verbose_name="Titre du site")
    description = models.TextField(verbose_name="Description du site (apparait dans les moteurs de cherche)")
    favicon = FilerImageField(verbose_name="Icône dans le navigateur", on_delete=models.DO_NOTHING,
                              related_name="favicon")
    logo = FilerImageField(verbose_name="Logo", on_delete=models.DO_NOTHING, related_name="logo")

    class Meta:
        verbose_name = "Configuration"

    def __str__(self):
        return self.title
