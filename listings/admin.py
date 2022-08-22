from django.contrib import admin
from listings.models import Band
from listings.models import Listing
class BandAdmin(admin.ModelAdmin):
    list_display = ("name","genere","year_formed")
class ListingsAdmin(admin.ModelAdmin):
    list_display = ("title","band")

admin.site.register(Band,BandAdmin)
admin.site.register(Listing,ListingsAdmin)

