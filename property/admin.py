from django.contrib import admin

from .models import Flat
from .models import Claim


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town', 'owners_phonenumber', 'owner_pure_phone')
    list_editable = ['new_building']
    list_filter = ('new_building',)
    raw_id_fields = ('liked_by',)


class ClaimAdmin(admin.ModelAdmin):
    search_fields = ('username', 'flat')
    raw_id_fields = ('flat',)
    list_display = ('username', 'flat', 'claim_text')


admin.site.register(Flat, FlatAdmin)
admin.site.register(Claim, ClaimAdmin)
