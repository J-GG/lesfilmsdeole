from django.db import models
from filer.fields.file import FilerFileField
from ckeditor.fields import RichTextField


class FooterContent(models.Model):
    """Content of the footer section."""

    text = RichTextField(blank=True, null=True, verbose_name="Texte")
    terms = FilerFileField(blank=True, null=True, verbose_name="Conditions générales de ventes",
                           on_delete=models.SET_NULL, related_name="terms")
    legal_notice = FilerFileField(blank=True, null=True, verbose_name="Mentions légales",
                                  on_delete=models.SET_NULL, related_name="legal_notice")

    class Meta:
        verbose_name = "Contenu"

    def __str__(self):
        return self.text
