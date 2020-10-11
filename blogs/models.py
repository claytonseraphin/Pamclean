from django.db import models
from datetime import datetime
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class Blogs(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(unique=True, null=False)
	body = models.TextField()
	cover = models.ImageField(upload_to='blogs')
	created_at = models.DateTimeField(default=datetime.now)


	def __str__(self):
		return self.title
	class Meta:
		verbose_name_plural='Blogs'


	def get_absolute_url(self):
		return reverse('blogs:blog_details', kwargs={'slug':self.slug})

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Blogs, self).save(*args, **kwargs)
