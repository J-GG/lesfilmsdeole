from django.db import models
from ckeditor.fields import RichTextField
from filer.fields.image import FilerImageField


class Configuration(models.Model):
    """Configuration of the website."""

    title = models.CharField(max_length=200, verbose_name="Titre du site")
    description = models.TextField(verbose_name="Description du site (apparait dans les moteurs de cherche)")
    favicon = FilerImageField(blank=True, null=True, verbose_name="Icône dans le navigateur", on_delete=models.SET_NULL,
                              related_name="favicon")
    logo = FilerImageField(blank=True, null=True, verbose_name="Logo", on_delete=models.SET_NULL, related_name="logo")
    analytics = models.TextField(blank=True, null=True, verbose_name="Code Google Analytics")

    class Meta:
        verbose_name = "Configuration"

    def __str__(self):
        return self.title
