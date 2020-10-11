from django.urls import path
from . import views

urlpatterns = [
	path('', views.BlogListView.as_view(), name="index"),
	path('blogs/<slug:slug>/', views.BlogDetailView.as_view(), name='blog_details')
	

]

app_name = 'blogs'
