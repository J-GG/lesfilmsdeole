from django.contrib import admin
from .models import HomeContent
from django.utils.text import Truncator


class HomeContentAdmin(admin.ModelAdmin):
    """Admin options for the `HomeContent` model."""

    list_display = ("title", "truncated_subtitle")

    def truncated_subtitle(self, section):
        """
        Truncates the subtitle and returns the 100 first characters.

        :param section: The section.
        :return: The 100 first characters of the subtitle.
        """
        return Truncator(section.heading).chars(100, truncate='...')

    truncated_subtitle.short_description = "Aperçu du sous-titre"


admin.site.register(HomeContent, HomeContentAdmin)
