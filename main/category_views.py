# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from models import Category
# Create your views here.

def get_categories(request):
	categories = Category.objects.all()
	return render(request, 'categories.html', {"categories": categories})
