from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from froala_editor import views
from django.views.generic import TemplateView

urlpatterns = [
	path('', TemplateView.as_view(template_name="homepage.html")),
    path('admin/', admin.site.urls),
    path('blogs/', include('blogs.urls', namespace='blogs')),
    path('products/', include('products.urls', namespace='products')),
    path('testimonials/', include('testimonials.urls', namespace='testimonials')),
    path('galri/', include('gallery-contenido.urls', namespace='gallery-contenido')),
    path('froala_editor/', include('froala_editor.urls')),
    #path('emoji/', include('emoji.urls')),
    path('instagram/', include('instagram_profile.urls')),
    path('galeria/', TemplateView.as_view(template_name="galeria.html")),
    path('gallery/', include('gallery.urls', namespace='gallery')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)