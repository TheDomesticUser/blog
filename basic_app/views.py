from django.shortcuts import render
from django.views.generic import (TemplateView, ListView,
                                    DetailView, CreateView, UpdateView, DeleteView)
from django.urls import reverse

class IndexView(TemplateView):
    template_name = 'basic_app/index.html'
