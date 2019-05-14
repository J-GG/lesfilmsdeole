from django.contrib import admin
from .models import PartnershipContent, Partner
from django.utils.text import Truncator


class PartnershipContentAdmin(admin.ModelAdmin):
    """Admin options for the `PartnershipContent` model."""

    list_display = ("title", "truncated_heading")

    def truncated_heading(self, section):
        """
        Truncates the heading and returns the 100 first characters.

        :param section: The section.
        :return: The 100 first characters of the heading.
        """
        return Truncator(section.heading).chars(100, truncate='...')

    truncated_heading.short_description = "Aperçu de l'entête"


admin.site.register(PartnershipContent, PartnershipContentAdmin)


class PartnerAdmin(admin.ModelAdmin):
    """Admin options for the `Partner` model."""

    list_display = ("name", "truncated_link", "order")

    def truncated_link(self, section):
        """
        Truncates the link and returns the 100 first characters.

        :param section: The section.
        :return: The 100 first characters of the link.
        """
        return Truncator(section.link).chars(100, truncate='...')

    truncated_link.short_description = "Aperçu du lien"


admin.site.register(Partner, PartnerAdmin)
