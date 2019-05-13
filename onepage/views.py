from django.shortcuts import render
from configuration.models import Configuration
from industries.models import IndustriesContent, Industry
from home.models import HomeContent
from aboutus.models import AboutUsContent
from portfolio.models import PortfolioContent, PortfolioMedia


def index(request):
    configuration = Configuration.objects.last()
    sections = dict()
    sections["home"] = {"content": HomeContent.objects.last()}
    sections["about_us"] = {"content": AboutUsContent.objects.last()}
    sections["industries"] = {"content": IndustriesContent.objects.last(), "industries": Industry.objects.all()}
    sections["portfolio"] = {"content": PortfolioContent.objects.last(), "medias": PortfolioMedia.objects.all()}
    return render(request, "onepage/index.html", locals())
