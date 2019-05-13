from django.db import models
from ckeditor.fields import RichTextField
import re
import requests
import json


class PortfolioContent(models.Model):
    """Content of the portfolio section."""

    title = models.CharField(max_length=200, verbose_name="Titre")
    heading = RichTextField(blank=True, null=True, verbose_name="Entête")

    class Meta:
        verbose_name = "Contenu"

    def filters_list(self):
        filters = []
        concatenated_filters = [filter for filter in PortfolioMedia.objects.values_list("filters", flat=True)]
        for filter in concatenated_filters:
            filters += filter.lower().split(" ")

        filters = list(dict.fromkeys(filters))
        return filters

    def __str__(self):
        return self.title


class PortfolioMedia(models.Model):
    """Represents a media to be displayed."""

    YOUTUBE_PATTERN = re.compile(r"youtube\.com/.*v=([^&]*)")
    VIMEO_PATTERN = re.compile(r"(https?:\/\/)?(www\.)?(player\.)?vimeo\.com\/([a-z]*\/)*([0-9]{6,11})[?]?.*")

    title = models.CharField(max_length=200, verbose_name="Titre")
    description = models.CharField(max_length=200, null=True, verbose_name="Description")
    filters = models.CharField(max_length=200, verbose_name="Filtres séparés par un espace")
    link = models.CharField(max_length=200, verbose_name="Lien vers l'image ou la vidéo")
    width = models.IntegerField(verbose_name="Largeur de la miniature dans le portfolio (ratio)")
    height = models.IntegerField(verbose_name="Hauteur de la miniature dans le portfolio (ratio)")
    columns = models.IntegerField(verbose_name="Nombre de colonnes de la miniature dans le portfolio")
    order = models.IntegerField(verbose_name="Ordre d'affichage (le plus grand en premier)")

    class Meta:
        verbose_name = "Média"
        ordering = ["-order"]

    def is_youtube_video(self):
        return True if PortfolioMedia.YOUTUBE_PATTERN.search(self.link) else False

    def is_vimeo_video(self):
        return True if PortfolioMedia.VIMEO_PATTERN.search(self.link) else False

    def thumbnail(self):
        if self.is_youtube_video():
            matches = PortfolioMedia.YOUTUBE_PATTERN.search(self.link)
            if matches:
                return "https://img.youtube.com/vi/{0}/maxresdefault.jpg".format(matches.group(1))
            else:
                return None
        elif self.is_vimeo_video():
            matches = PortfolioMedia.VIMEO_PATTERN.search(self.link)
            if matches:
                response = requests.get('http://www.vimeo.com/api/v2/video/{0}.json'.format(matches.group(5)))
                if response.ok:
                    return json.loads(response.content)[0]["thumbnail_large"]
                else:
                    return None
            else:
                return None
        else:
            return self.link

    def filters_as_list(self):
        return self.filters.split(" ")

    def __str__(self):
        return self.title
