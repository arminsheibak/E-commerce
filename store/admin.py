from django.contrib import admin
from . import models


@admin.register(models.Product)
class PorductAdmin(admin.ModelAdmin):
    list_display = ["title", "unit_price", "inventory_status"]
    list_editable = ["unit_price"]
    list_per_page = 10

    @admin.display(ordering="inventory")
    def inventory_status(self, product: models.Product):
        if product.inventory < 10:
            return "Low"
        return "OK"


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "membership"]
    list_editable = ["membership"]
    list_select_related = ["user"]
    list_per_page = 10
    search_fields = ["first_name__istartswith", "last_name__istartswith"]


admin.site.register(models.Collection)


class OrderItemInline(admin.StackedInline):
    model = models.OrderItem
    extra = 0


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "placed_at", "customer"]
    inlines = [OrderItemInline]
