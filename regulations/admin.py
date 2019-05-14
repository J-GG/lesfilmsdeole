from django.contrib import admin
from .models import RegulationsContent
from django.utils.text import Truncator


class RegulationsContentAdmin(admin.ModelAdmin):
    """Admin options for the `RegulationsContent` model."""

    list_display = ("title", "truncated_heading")

    def truncated_heading(self, section):
        """
        Truncates the heading and returns the 100 first characters.

        :param section: The section.
        :return: The 100 first characters of the heading.
        """
        return Truncator(section.heading).chars(100, truncate='...')

    truncated_heading.short_description = "Aperçu de l'entête"


admin.site.register(RegulationsContent, RegulationsContentAdmin)
