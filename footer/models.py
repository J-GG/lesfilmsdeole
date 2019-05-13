from django.db import models
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField
from ckeditor.fields import RichTextField


class FooterContent(models.Model):
    """Content of the footer section."""

    text = RichTextField(blank=True, null=True, verbose_name="Texte")
    terms = FilerFileField(blank=True, null=True, verbose_name="Conditions générales de ventes",
                           on_delete=models.DO_NOTHING, related_name="terms")
    legal_notice = FilerFileField(blank=True, null=True, verbose_name="Mentions légales",
                                  on_delete=models.DO_NOTHING, related_name="legal_notice")
    background = FilerImageField(blank=True, null=True, verbose_name="Image de fond", on_delete=models.DO_NOTHING,
                                 related_name="background")

    class Meta:
        verbose_name = "Contenu"

    def __str__(self):
        return self.text
