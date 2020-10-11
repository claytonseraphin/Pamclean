from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from products.models import Products
from taggit.models import Tag, TaggedItem
from django.contrib.contenttypes.models import ContentType
from django.template.defaultfilters import slugify

# Create your views here.

class TagIndexView(ListView):
	template_name = 'products/index.html'
	model = Products
	context_object_name = 'products'

	def get_queryset(self):
		return Products.objects.filter(tags__slug=self.kwargs.get('slug'))
""""
def tagged(request, slug):
	tag = get_object_or_404(Tag, slug=slug)
	products_related = Products.objects.filter(tags=tag)
	context = {
		'products_related':products_related,
		'tag':tag,
	}
	return render(request, 'products/index.html')
"""
class ProductListView(ListView):
	model = Products

	template_name = 'products/index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['common_tags'] = Products.tags.most_common()[:4]
		return context

class ProductDetailView(DetailView):
	model = Products
	template_name = 'products/detail.html'
	context_object_name = 'products'

	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    context['common_tags'] = Products.tags.most_common()[:4]
	    context['related_items'] = self.object.tags.similar_objects()[:4]
	    return context
		
