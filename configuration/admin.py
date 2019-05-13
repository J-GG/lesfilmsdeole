from django.contrib import admin
from .models import Configuration
from django.utils.text import Truncator


class ConfigurationAdmin(admin.ModelAdmin):
    """Admin options for the `Configuration` model."""

    list_display = ("title", "truncated_description")

    def truncated_description(self, configuration):
        """
        Truncates the subtitle and returns the 100 first characters.

        :param configuration: The configuration.
        :return: The 100 first characters of the description.
        """
        return Truncator(configuration.description).chars(100, truncate='...')

    truncated_description.short_description = "Aperçu du sous-titre"


admin.site.register(Configuration, ConfigurationAdmin)
