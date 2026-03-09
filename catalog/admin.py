from django.contrib import admin
from django.utils.html import mark_safe
from .models import Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3
    fields = ['image', 'is_main', 'order', 'preview']
    readonly_fields = ['preview']

    def preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" height="80">')
        return "Нет фото"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'status', 'show_on_main', 'order', 'main_photo']
    list_editable = ['status', 'show_on_main', 'order']
    list_filter = ['status', 'show_on_main']
    search_fields = ['name', 'material']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline]

    def main_photo(self, obj):
        img = obj.main_image
        if img:
            return mark_safe(f'<img src="{img.image.url}" height="50">')
        return "Нет фото"
    main_photo.short_description = "Фото"