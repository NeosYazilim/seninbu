from django.contrib import admin

from product.models import Category, Images, Product

class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 5
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category','image_tag', 'price', 'status']
    list_filter = ['category','status']
    inlines = [ProductImageInline]
    readonly_fields = ('image_tag',)

class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'product','image_tag']
    readonly_fields = ('image_tag',)


admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Images, ImageAdmin)
