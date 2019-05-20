from django.contrib import admin
from .models import AboutUsContent, AboutUsInfo
from django.utils.text import Truncator


class AboutUsContentAdmin(admin.ModelAdmin):
    """Admin options for the `AboutUsContent` model."""

    list_display = ("title", "truncated_heading")

    def truncated_heading(self, section):
        """
        Truncates the heading and returns the 100 first characters.

        :param section: The section.
        :return: The 100 first characters of the heading.
        """
        return Truncator(section.heading).chars(100, truncate='...')

    truncated_heading.short_description = "Aperçu de l'entête"


admin.site.register(AboutUsContent, AboutUsContentAdmin)


class AboutUsInfoAdmin(admin.ModelAdmin):
    """Admin options for the `AboutUsInfo` model."""

    list_display = ("title", "truncated_description", "icon", "order")
    search_fields = ("title", "description", "icon", "order")

    def truncated_description(self, about_us_info):
        """
        Truncates the description and returns the 100 first characters.

        :param about_us_info: The information.
        :return: The 100 first characters of the description.
        """
        return Truncator(about_us_info.description).chars(100, truncate='...')

    truncated_description.short_description = "Aperçu de la description"


admin.site.register(AboutUsInfo, AboutUsInfoAdmin)
