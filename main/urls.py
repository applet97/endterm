from django.conf.urls import url
from django.contrib import admin
import category_views, product_views

urlpatterns = [
	url(r'^categories/', category_views.get_categories),
    url(r'^create_product/', product_views.create),
]
