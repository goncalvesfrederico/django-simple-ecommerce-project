from django.contrib import admin
from product.models import Product, Variation

@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
    list_display = "id", "nome", "preco"
    list_display_links = "nome",
    search_fields = "nome",
    list_per_page = 10


class VariationInline(admin.TabularInline):
    model = Variation
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = "id", "nome", "slug", "preco_marketing"
    list_display_links = "id", "nome",
    search_fields = "id", "nome", "slug",
    list_per_page = 10
    ordering = "-id",
    prepopulated_fields = {
        "slug": ("nome",),
    }
    inlines = VariationInline,