from django.shortcuts import render, render_to_response
from configuration.models import Configuration
from home.models import HomeContent
from aboutus.models import AboutUsContent, AboutUsInfo
from industries.models import IndustriesContent, Industry
from portfolio.models import PortfolioContent, PortfolioMedia
from pricing.models import PricingContent, Price
from equipment.models import EquipmentContent, Equipment
from testimonials.models import TestimonialsContent, Testimonial
from regulations.models import RegulationsContent
from contact.models import ContactContent
from partnership.models import PartnershipContent, Partner
from footer.models import FooterContent


def index(request):
    configuration = Configuration.objects.last()
    sections = dict()
    sections["home"] = {"content": HomeContent.objects.last()}
    sections["about_us"] = {"content": AboutUsContent.objects.last(), "infos": AboutUsInfo.objects.all()}
    sections["industries"] = {"content": IndustriesContent.objects.last(), "industries": Industry.objects.all()}
    sections["portfolio"] = {"content": PortfolioContent.objects.last(), "medias": PortfolioMedia.objects.all()}
    sections["pricing"] = {"content": PricingContent.objects.last(), "prices": Price.objects.all()}
    sections["equipment"] = {"content": EquipmentContent.objects.last(), "equipments": Equipment.objects.all()}
    sections["testimonials"] = {"content": TestimonialsContent.objects.last(),
                                "testimonials": Testimonial.objects.all()}
    sections["regulations"] = {"content": RegulationsContent.objects.last()}
    sections["contact"] = {"content": ContactContent.objects.last()}
    sections["partnership"] = {"content": PartnershipContent.objects.last(), "partners": Partner.objects.all()}
    sections["footer"] = {"content": FooterContent.objects.last()}
    return render(request, "onepage/index.html", locals())


def page_not_found(request, exception):
    configuration = Configuration.objects.last()
    response = render_to_response('404.html', locals())
    response.status_code = 404
    return response
