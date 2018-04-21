# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from models import Product, Category
# Create your views here.

def add_product(request, category_id):
	data = request.POST
	new_title = data.get("new_title")
	category = Category.objects.get(pk=category_id)
	product = Product(title=new_title, category=category)
	product.save()
	products = Product.objects.filter(category=category, is_active=True)
	return render(request, 'products.html', {"products": products, "category": category})

def get_products(request, category_id):
	category = Category.objects.get(pk=category_id)
	products = Product.objects.filter(category=category, is_active=True)
	return render(request, 'products.html', {"products": products, "category": category})

def edit_product(request, product_id):
	product = Product.objects.get(pk=product_id)
	return render(request, 'edit_product.html', {"product": product})

def update_product(request, product_id):
	data = request.POST
	product = Product.objects.get(pk=product_id)
	new_title = data.get("new_title", product.title)
	product.title = new_title
	product.save()
	category = product.category
	products = Product.objects.filter(category=category, is_active=True)
	return render(request, 'products.html', {"products": products, "category": category})

def delete_product(request, product_id):
	product = Product.objects.get(pk=product_id)
	product.is_active = False
	product.save()
	category = product.category
	products = Product.objects.filter(category=category, is_active=True)
	return render(request, 'products.html', {"products": products, "category": category})

