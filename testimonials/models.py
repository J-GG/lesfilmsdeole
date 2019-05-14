from django.db import models
from filer.fields.image import FilerImageField
from ckeditor.fields import RichTextField


class TestimonialsContent(models.Model):
    """Content of the testimonials section."""

    title = models.CharField(max_length=200, verbose_name="Titre")
    heading = RichTextField(blank=True, null=True, verbose_name="Entête")
    background = FilerImageField(blank=True, null=True, verbose_name="Image de fond", on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Contenu"

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    """Represents an testimonial to be displayed."""

    title = models.CharField(max_length=200, verbose_name="Titre")
    subtitle = models.CharField(max_length=250, blank=True, null=True, verbose_name="Sous-titre")
    logo = FilerImageField(max_length=50, blank=True, null=True, verbose_name="Logo", on_delete=models.SET_NULL)
    link = models.URLField(blank=True, null=True, verbose_name="Lien")
    order = models.IntegerField(verbose_name="Ordre d'affichage")

    class Meta:
        verbose_name = "Témoignage"
        ordering = ["order"]

    def __str__(self):
        return self.title
