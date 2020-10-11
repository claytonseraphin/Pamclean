from django import forms
from testimonials.models import Testimonials
from froala_editor.widgets import FroalaEditor


class TestimonialForm(forms.ModelForm):
	content = forms.CharField(widget=FroalaEditor)
	
	class Meta:
		model = Testimonials
		fields = ('title', 'content', 'client')