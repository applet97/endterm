# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Category(models.Model):
	"""
	"""
	title = models.CharField(max_length=100)

	def __unicode__(self):
		return "{}".format(self.title)

	def full(self):
		obj = {
			"title": self.title
		}
		return obj

	class Meta:
		verbose_name_plural = "Categories"

class Product(models.Model):
	"""
	"""
	title = models.CharField(max_length=100)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	def __unicode__(self):
		return "{} ({})".format(self.title, self.category)

	def full(self):
		obj = {
			"title": self.title
		}
		return obj