from django.shortcuts import render
from industries.models import IndustriesContent, Industry


def index(request):
    sections = dict()
    sections["industries"] = {"content": IndustriesContent.objects.last(), "industries": Industry.objects.all()}
    return render(request, "onepage/index.html", locals())
