from rest_framework import serializers
from .models import Testimonials


class TestimonialSerializer(serializers.ModelSerializer):
	model = Testimonials
	fields = ['title']