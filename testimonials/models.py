from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from datetime import datetime
from froala_editor.fields import FroalaField

# Create your models here.

class Testimonials(models.Model):
	title = models.CharField(max_length=300)
	content = FroalaField(theme='dark', options={'toolbarInline':True})
	client = models.CharField(max_length=200)
	slug = models.SlugField(unique=True)
	created_at = models.DateTimeField(default=datetime.now)

	def __str__():
		return self.title

	def get_absolute_url(self):
		return reverse('testimonials:testimonial_detail', kwargs={'slug':self.slug})

	class Meta:
		verbose_name_plural = 'Testimonials'

	def save(self, *args, **kwargs):
		self.slug = slugify("{obj.title}-{obj.client}".format(obj=self))
		super(Testimonials, self).save(*args, **kwargs)
