from django.contrib import admin
from .models import PortfolioContent, PortfolioMedia
from django.utils.text import Truncator


class PortfolioContentAdmin(admin.ModelAdmin):
    """Admin options for the `PortfolioContent` model."""

    list_display = ("title", "truncated_heading")

    def truncated_heading(self, section):
        """
        Truncates the heading and returns the 100 first characters.

        :param section: The section.
        :return: The 100 first characters of the heading.
        """
        return Truncator(section.heading).chars(100, truncate='...')

    truncated_heading.short_description = "Aperçu de l'entête"


admin.site.register(PortfolioContent, PortfolioContentAdmin)


class PortfolioMediaAdmin(admin.ModelAdmin):
    """Admin options for the `PortfolioMedia` model."""

    list_display = ("title", "truncated_description", "order")
    search_fields = ("title", "description", "order")

    def truncated_description(self, media):
        """
        Truncates the description and returns the 100 first characters.

        :param media: The media.
        :return: The 100 first characters of the description.
        """
        return Truncator(media.description).chars(100, truncate='...')

    truncated_description.short_description = "Aperçu de la description"


admin.site.register(PortfolioMedia, PortfolioMediaAdmin)
