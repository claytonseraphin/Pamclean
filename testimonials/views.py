from django.shortcuts import render
from testimonials.models import Testimonials
from testimonials.form import TestimonialForm
from rest_framework import viewsets
from .serializers import TestimonialSerializer

from django.views.generic import ListView, CreateView,DetailView

from .models import Testimonials

# Create your views here.

class TestimonialListView(ListView):
	model = Testimonials
	template_name = 'testimonials/index.html'


class TestimonialCreateView(CreateView):
	model = Testimonials
	form_class = TestimonialForm
	template_name = 'testimonials/testimonial_form.html'
	redirect_field_name = '/testimonials/index.html'
	

class TestimonialDetailView(DetailView):
	model = Testimonials
	template_name = 'testimonials/testimonial_detail.html'

