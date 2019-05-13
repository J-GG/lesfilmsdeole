from django.db import models
from ckeditor.fields import RichTextField
from filer.fields.image import FilerImageField


class AboutUsContent(models.Model):
    """Content of the about us section."""

    title = models.CharField(max_length=200, verbose_name="Titre")
    heading = RichTextField(blank=True, null=True, verbose_name="Entête")
    first_item_image = FilerImageField(blank=True, null=True, verbose_name="Image du premier point",
                                       on_delete=models.SET_NULL, related_name="first_item_image")
    first_item_title = models.CharField(blank=True, null=True, max_length=200, verbose_name="Titre du premier point")
    first_item_description = RichTextField(blank=True, null=True, verbose_name="Description du premier point")
    second_item_image = FilerImageField(blank=True, null=True, verbose_name="Image du second point",
                                        on_delete=models.SET_NULL, related_name="second_item_image")
    second_item_title = models.CharField(blank=True, null=True, max_length=200, verbose_name="Titre du second point")
    second_item_description = RichTextField(blank=True, null=True, verbose_name="Description du second point")
    third_item_image = FilerImageField(blank=True, null=True, verbose_name="Image du troisième point",
                                       on_delete=models.SET_NULL, related_name="third_item_image")
    third_item_title = models.CharField(blank=True, null=True, max_length=200, verbose_name="Titre du troisième point")
    third_item_description = RichTextField(blank=True, null=True, verbose_name="Description du troisième point")
    more_title = models.CharField(blank=True, null=True, max_length=200,
                                  verbose_name="Titre du bloc d'informations supplémentaires")
    more_content = RichTextField(blank=True, null=True, verbose_name="Contenu du bloc d'informations supplémentaires")

    class Meta:
        verbose_name = "Contenu"

    def __str__(self):
        return self.title
