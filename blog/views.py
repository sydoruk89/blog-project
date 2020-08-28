from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blog

class HomePageView(ListView):
    template_name = "home.html"
    model = Blog

class PostPageView(DetailView):
    template_name = "post_detail.html"
    model = Blog