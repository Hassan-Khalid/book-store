from django.shortcuts import render
from django.views.generic import  TemplateView
# Create your views here.

class mainpage(TemplateView):
    template_name = 'user/index.html'