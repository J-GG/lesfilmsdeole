from django.shortcuts import render
from configuration.models import Configuration
from industries.models import IndustriesContent, Industry
from home.models import HomeContent
from aboutus.models import AboutUsContent
from portfolio.models import PortfolioContent, PortfolioMedia
from contact.models import ContactContent
from partnership.models import PartnershipContent, Partner
from footer.models import FooterContent


def index(request):
    configuration = Configuration.objects.last()
    sections = dict()
    sections["home"] = {"content": HomeContent.objects.last()}
    sections["about_us"] = {"content": AboutUsContent.objects.last()}
    sections["industries"] = {"content": IndustriesContent.objects.last(), "industries": Industry.objects.all()}
    sections["portfolio"] = {"content": PortfolioContent.objects.last(), "medias": PortfolioMedia.objects.all()}
    sections["contact"] = {"content": ContactContent.objects.last()}
    sections["partnership"] = {"content": PartnershipContent.objects.last(), "partners": Partner.objects.all()}
    sections["footer"] = {"content": FooterContent.objects.last()}
    return render(request, "onepage/index.html", locals())
