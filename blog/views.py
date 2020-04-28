from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import post # lay class post tu file database models

class BlogListView(ListView):
    model = post
    template_name = 'home.html'