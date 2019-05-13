from django.contrib import admin
from .models import FooterContent
from django.utils.text import Truncator


class FooterContentAdmin(admin.ModelAdmin):
    """Admin options for the `FooterContent` model."""

    list_display = ("truncated_text",)

    def truncated_text(self, section):
        """
        Truncates the heading and returns the 100 first characters.

        :param section: The section.
        :return: The 100 first characters of the heading.
        """
        return Truncator(section.text).chars(100, truncate='...')

    truncated_text.short_description = "Aperçu du texte"


admin.site.register(FooterContent, FooterContentAdmin)
