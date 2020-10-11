from django.shortcuts import render
from django.views.generic import ListView, TemplateView
import os
from django.conf import settings 
from django.shortcuts import render
from instagram_profile.models import Post

# Create your views here.


class GalleryListView(ListView):
	model = Post
	template_name = 'gallery-contenido/ig.html'
	context_object_name = 'posts'

