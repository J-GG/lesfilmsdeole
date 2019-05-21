from django.db import models
from ckeditor.fields import RichTextField
from filer.fields.image import FilerImageField


class ContactContent(models.Model):
    """Content of the contact section."""

    title = models.CharField(max_length=200, verbose_name="Titre")
    heading = RichTextField(blank=True, null=True, verbose_name="Entête")
    background = FilerImageField(blank=True, null=True, verbose_name="Image de fond",
                                 on_delete=models.SET_NULL, related_name="contact_background")
    address = models.CharField(blank=True, null=True, max_length=200, verbose_name="Adresse")
    phone = models.CharField(blank=True, null=True, max_length=200, verbose_name="Téléphone")
    email = models.EmailField(blank=True, null=True, max_length=200, verbose_name="Adresse email")
    facebook_plugin = models.URLField(blank=True, null=True, max_length=200, verbose_name="Lien plugin FB")
    facebook = models.URLField(blank=True, null=True, max_length=200, verbose_name="Lien FB")
    youtube = models.URLField(blank=True, null=True, max_length=200, verbose_name="Lien Youtube")
    vimeo = models.URLField(blank=True, null=True, max_length=200, verbose_name="Lien Viméo")
    email_success_message = models.CharField(max_length=250,
                                             verbose_name="Message affiché en cas de succès à la soumission du formulaire de contact")
    email_error_message = models.CharField(max_length=250,
                                           verbose_name="Message affiché en cas d'échec à la soumission du formulaire de contact")

    class Meta:
        verbose_name = "Contenu"

    def __str__(self):
        return self.title
