from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Item

# Create your views here.

class CategoryLV(ListView):
    model = Category

class CategoryDV(DetailView):
    model = Category

class ItemDV(DetailView):
    model = Item

