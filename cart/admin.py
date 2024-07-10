from django.contrib import admin
from cart.models import Order, OrderItems

@admin.register(OrderItems)
class OrderItemsAdmin(admin.ModelAdmin):
    list_display = "order", "product", "variation", "price", "quantity"
    list_display_links = "order",
    search_fields = "order", "product",
    list_per_page = 10


class OrderItemsInline(admin.TabularInline):
    model = OrderItems
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = "pk", "total", "status"
    list_display_links = "pk",
    search_fields = "pk", "total", "status",
    list_per_page = 10
    ordering = "-pk",
    inlines = OrderItemsInline,