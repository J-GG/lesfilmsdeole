from django.contrib import admin
from .models import TestimonialsContent, Testimonial
from django.utils.text import Truncator


class TestimonialsContentAdmin(admin.ModelAdmin):
    """Admin options for the `TestimonialsContent` model."""

    list_display = ("title", "truncated_heading")

    def truncated_heading(self, section):
        """
        Truncates the heading and returns the 100 first characters.

        :param section: The section.
        :return: The 100 first characters of the heading.
        """
        return Truncator(section.heading).chars(100, truncate='...')

    truncated_heading.short_description = "Aperçu de l'entête"


admin.site.register(TestimonialsContent, TestimonialsContentAdmin)


class TestimonialAdmin(admin.ModelAdmin):
    """Admin options for the `Industry` model."""

    list_display = ("title", "truncated_subtitle", "order")
    search_fields = ("title", "subtitle")

    def truncated_subtitle(self, testimonial):
        """
        Truncates the subtitle and returns the 100 first characters.

        :param testimonial: The testimonial.
        :return: The 100 first characters of the subtitle.
        """
        return Truncator(testimonial.subtitle).chars(100, truncate='...')

    truncated_subtitle.short_description = "Aperçu du sous-titre"


admin.site.register(Testimonial, TestimonialAdmin)
