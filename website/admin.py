from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Package, Location


class PackageAdmin(SummernoteModelAdmin):
    list_display = ('package', )
    list_display_links = ('package', )
    search_fields = ('package', )
    list_per_page = 25
    summernote_fields = ('description', 'services')


class LocationAdmin(admin.ModelAdmin):
    list_display = ('branch_name', 'zip_code')
    list_display_links = ('branch_name', 'zip_code')
    search_fields = ('branch_name', )
    list_per_page = 25


# Register your models here.
admin.site.register(Package, PackageAdmin)
admin.site.register(Location, LocationAdmin)
