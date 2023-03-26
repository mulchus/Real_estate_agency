from django.contrib import admin

from .models import Flat
from .models import Claim
from .models import Owner


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner', 'owners_phonenumber')
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town', 'owners_phonenumber',
                    'owner_pure_phone')
    list_editable = ['new_building']
    list_filter = ('new_building',)
    raw_id_fields = ('liked_by',)


class OwnerAdmin(admin.ModelAdmin):
    search_fields = ['owner', 'flat__address', 'owner_pure_phone']
    raw_id_fields = ('flat',)
    list_display = ('owner', 'owner_pure_phone', 'get_flats')

    def get_flats(self, obj):
        return ", ".join([flat.__str__() for flat in obj.flat.all()])


class ClaimAdmin(admin.ModelAdmin):
    search_fields = ['username__username', 'flat__address']
    raw_id_fields = ('flat',)
    list_display = ('username', 'flat', 'claim_text')


admin.site.register(Flat, FlatAdmin)
admin.site.register(Claim, ClaimAdmin)
admin.site.register(Owner, OwnerAdmin)
