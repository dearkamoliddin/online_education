from django.shortcuts import render
from django.views.generic import TemplateView


class BlogListView(TemplateView):
    template_name = 'blogs/blog.html'


class BlogDetailView(TemplateView):
    template_name = 'blogs/single.html'
