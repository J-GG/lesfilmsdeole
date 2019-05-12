from django.contrib import admin
from .models import IndustriesContent, Industry
from django.utils.text import Truncator


class IndustriesContentAdmin(admin.ModelAdmin):
    """Admin options for the `IndustriesContent` model."""

    list_display = ("title", "truncated_heading")

    def truncated_heading(self, section):
        """
        Truncates the heading and returns the 100 first characters.

        :param section: The section.
        :return: The 100 first characters of the heading.
        """
        return Truncator(section.heading).chars(100, truncate='...')

    truncated_heading.short_description = "Aperçu de l'entête"


admin.site.register(IndustriesContent, IndustriesContentAdmin)


class IndustryAdmin(admin.ModelAdmin):
    """Admin options for the `Industry` model."""

    list_display = ("name", "truncated_description", "icon", "order")
    search_fields = ("name", "description", "icon", "order")

    def truncated_description(self, industry):
        """
        Truncates the description and returns the 100 first characters.

        :param industry: The industry.
        :return: The 100 first characters of the description.
        """
        return Truncator(industry.description).chars(100, truncate='...')

    truncated_description.short_description = "Aperçu de la description"


admin.site.register(Industry, IndustryAdmin)
