from django.conf.urls import url
from django.contrib import admin
import category_views, product_views

urlpatterns = [
	url(r'^categories/', category_views.get_categories, name="categories"),
	url(r'^get_products/(?P<category_id>\d+)/', product_views.get_products, name="get_products"),
    url(r'^edit_product/(?P<product_id>\d+)/', product_views.edit_product, name="edit_product"),
    url(r'^update_product/(?P<product_id>\d+)/', product_views.update_product, name="update_product"),
    url(r'^delete_product/(?P<product_id>\d+)/', product_views.delete_product, name="delete_product"),
    url(r'^add_product/(?P<category_id>\d+)/', product_views.add_product, name="add_product"),
]
