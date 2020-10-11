from django.urls import path
from . import views

app_name = 'products'

urlpatterns= [
	path('', views.ProductListView.as_view(), name="index"),
	path('detail/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
	path('tag/<slug:slug>/', views.TagIndexView.as_view(), name="tagged"),
]
