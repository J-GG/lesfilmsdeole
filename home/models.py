from django.db import models
from ckeditor.fields import RichTextField
from filer.fields.image import FilerImageField


class HomeContent(models.Model):
    """Content of the home section."""

    title = models.CharField(max_length=200, verbose_name="Titre")
    subtitle = RichTextField(blank=True, null=True, verbose_name="Sous-titre")
    video = models.CharField(blank=True, null=True, max_length=200, verbose_name="Lien de la vidéo")
    background = FilerImageField(blank=True, null=True, verbose_name="Image de fond", on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Contenu"

    def __str__(self):
        return self.title
