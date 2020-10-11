from django.urls import path, include
from testimonials import views




app_name = 'testimonials'


urlpatterns = [
	path('', views.TestimonialListView.as_view(), name='index'),
	path('create/', views.TestimonialCreateView.as_view(), name='testimonial_create'),
	path('<slug:slug>/', views.TestimonialDetailView.as_view(), name='testimonial_detail'),
	
]