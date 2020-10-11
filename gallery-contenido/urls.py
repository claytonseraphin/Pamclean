from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static

app_name = 'gallery-contenido'

urlpatterns=[
	#path('', views.index, name="index"),
	path('', views.GalleryListView.as_view(template_name="gallery-contenido/ig.html"), name='add_ig')
	#path('', TemplateView.as_view(template_name="gallery/ig.html"), name='add_ig'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




