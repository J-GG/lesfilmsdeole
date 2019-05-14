from django.db import models
from ckeditor.fields import RichTextField


class RegulationsContent(models.Model):
    """Content of the regulations section."""

    title = models.CharField(max_length=200, verbose_name="Titre")
    heading = RichTextField(blank=True, null=True, verbose_name="Entête")
    text_before_scenarios = RichTextField(blank=True, null=True, verbose_name="Texte avant le bloc scénario")
    scenario_title = models.CharField(blank=True, null=True, max_length=200, verbose_name="Titre du bloc scénario")
    scenario_inhabited_tooltip = models.CharField(blank=True, null=True, max_length=200,
                                                  verbose_name="Tooltip pour \"Zone peuplée\"")
    scenario_in_sight_tooltip = models.CharField(blank=True, null=True, max_length=200,
                                                 verbose_name="Tooltip pour \"Drone en visuel\"")
    scenario_no = RichTextField(blank=True, null=True, verbose_name="Texte \"Aucun scénario\"")
    scenario_1 = RichTextField(blank=True, null=True, verbose_name="Texte \"Scénario 1\"")
    scenario_2 = RichTextField(blank=True, null=True, verbose_name="Texte \"Scénario 2\"")
    scenario_3 = RichTextField(blank=True, null=True, verbose_name="Texte \"Scénario 3\"")
    scenario_4 = RichTextField(blank=True, null=True, verbose_name="Texte \"Scénario 4\"")
    text_after_scenarios = RichTextField(blank=True, null=True, verbose_name="Texte après le bloc scénario")

    class Meta:
        verbose_name = "Contenu"

    def __str__(self):
        return self.title
