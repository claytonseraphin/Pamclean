
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from taggit.managers import TaggableManager

# Create your models here.
class Products(models.Model):
	name = models.CharField(max_length=200)
	photo = models.ImageField(upload_to='products')
	detail = models.TextField()
	slug = models.SlugField(unique=True)
	tags = TaggableManager()

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('products:product_detail', kwargs={'slug':self.slug})
		
	class Meta:
		verbose_name_plural = 'Products'


	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Products, self).save(*args, **kwargs)