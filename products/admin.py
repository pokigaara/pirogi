from django.contrib import admin
from .models import *


class MyAdmin(admin.ModelAdmin):
    list_display = ['name', 'size', 'categories', 'price', 'slivki', 'price_sliv', 'discount']
    list_filter = ['size', 'categories']
    list_editable = ['price', 'slivki', 'price_sliv', 'discount']


admin.site.register(Products, MyAdmin)
admin.site.register(Size)
admin.site.register(Categories)






