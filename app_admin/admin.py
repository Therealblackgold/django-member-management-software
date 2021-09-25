from django.contrib import admin
from .models import Payment


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('member', 'month', 'amount', 'date')
    list_display_links = ('member', )
    search_fields = ('member', 'date')
    list_per_page = 25


admin.site.register(Payment, PaymentAdmin)
