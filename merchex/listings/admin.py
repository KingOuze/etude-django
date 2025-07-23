from django.contrib import admin # type: ignore
from .models import Band, Listing


class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')

class ListingAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'description', 'sold', 'type')


admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)
