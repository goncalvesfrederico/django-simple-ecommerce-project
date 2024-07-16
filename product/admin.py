from django.contrib import admin
from product.models import Product, Variation

@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
    list_display = "id", "name", "formatted_price", "formatted_promotion_price"
    list_display_links = "name",
    search_fields = "name",
    list_per_page = 10


class VariationInline(admin.TabularInline):
    model = Variation
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = "id", "name", "formatted_price", "formatted_promotion_price",
    list_display_links = "id", "name",
    search_fields = "id", "name", "slug",
    list_per_page = 10
    ordering = "-id",
    prepopulated_fields = {
        "slug": ("name",),
    }
    inlines = VariationInline,