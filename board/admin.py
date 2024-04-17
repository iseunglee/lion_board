from django.contrib import admin
from board.models import Category, Item
# Register your models here.

class ItemInline(admin.StackedInline):
    model = Item
    extra = 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (ItemInline,)
    list_display = ('id', 'ct_name')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'it_name', 'description')