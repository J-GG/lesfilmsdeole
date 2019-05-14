from django.contrib import admin
from .models import PricingContent, Price
from django.utils.text import Truncator


class PricingContentAdmin(admin.ModelAdmin):
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


admin.site.register(PricingContent, PricingContentAdmin)


class PriceAdmin(admin.ModelAdmin):
    """Admin options for the `Industry` model."""

    list_display = ("name", "truncated_subtitle", "order")
    search_fields = ("name", "subtitle", "order")

    def truncated_subtitle(self, price):
        """
        Truncates the subtitle and returns the 100 first characters.

        :param price: The price.
        :return: The 100 first characters of the description.
        """
        return Truncator(price.subtitle).chars(100, truncate='...')

    truncated_subtitle.short_description = "Aperçu de la description"


admin.site.register(Price, PriceAdmin)
