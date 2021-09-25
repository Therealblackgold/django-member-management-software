from django.contrib import admin
from .models import Member, Spouse, Family, MembershipNumber, Document


class MemberAdmin(admin.ModelAdmin):
    # fields = ('admin_photo', 'title', 'image')
    list_display = ['id', 'first_name', 'last_name', 'status']
    list_display_links = ['id', 'first_name', 'last_name']
    search_fields = ('first_name', 'last_name', 'status', 'email', 'phone',
                     'phone_2', 'street', 'town', 'city')
    list_per_page = 25


class MembershipNumberAdmin(admin.ModelAdmin):
    # fields = ('admin_photo', 'title', 'image')
    list_display = ['id', 'user', 'id_number', 'slug']
    list_display_links = ['id', 'user', 'id_number']
    search_fields = ('id_number', 'user')
    list_per_page = 25


class DocumentAdmin(admin.ModelAdmin):
    # fields = ('admin_photo', 'title', 'image')
    list_display = ['membership_no', 'title', 'docfile', 'created']
    list_display_links = ['membership_no', 'title', 'docfile', 'created']


class SpouseAdmin(admin.ModelAdmin):
    exclude = ['slug']
    list_display = ['first_name', 'last_name', 'membership_no', 'id_no']
    list_display_links = ['first_name']
    search_fields = ('first_name', 'last_name', 'id_no', 'email', 'phone',
                     'phone_2', 'street', 'town', 'city', 'membership_no')
    list_per_page = 25


class FamilyAdmin(admin.ModelAdmin):
    exclude = ['slug']
    list_display = ['first_name', 'last_name', 'membership_no', 'id_no']
    list_display_links = ['first_name']
    search_fields = ('first_name', 'last_name', 'id_no', 'email', 'phone',
                     'phone_2', 'street', 'town', 'city', 'membership_no')
    list_per_page = 25


# Register your models here.
admin.site.register(MembershipNumber, MembershipNumberAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Spouse, SpouseAdmin)
admin.site.register(Family, FamilyAdmin)
