from django.shortcuts import render
from industries.models import IndustriesContent, Industry
from aboutus.models import AboutUsContent


def index(request):
    sections = dict()
    sections["about_us"] = {"content": AboutUsContent.objects.last()}
    sections["industries"] = {"content": IndustriesContent.objects.last(), "industries": Industry.objects.all()}
    return render(request, "onepage/index.html", locals())
