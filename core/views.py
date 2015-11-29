from django.shortcuts import render
from django.views.generic.base import TemplateView
import core.models as coremodels
# Create your views here.

class LandingView(TemplateView):
    template_name = 'base/index.html'


# Create your views here.
