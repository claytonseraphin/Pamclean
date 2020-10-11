from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogs
from django.views.generic import ListView, DetailView

# Create your views here.
class BlogListView(ListView):
	model = Blogs
	template_name = 'blogs/index.html'
	context_object_name = 'bloglists'

class BlogDetailView(DetailView):
	model = Blogs
	template_name = 'blogs/details.html'
