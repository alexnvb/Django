from django.contrib import admin
from .models import *

# Register your models here.

# class CategoryAdmin (admin.ModelAdmin):
#     list_display = [field.name for field in Category._meta.fields]
#
#     class Meta:
#         model = Category
#
# admin.site.register(Category, CategoryAdmin)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Item)
admin.site.register(ImageItem)
