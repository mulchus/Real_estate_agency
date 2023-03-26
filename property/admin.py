from django.contrib import admin

from .models import Flat
from .models import Claim
from .models import Owner


class OwnersInline(admin.TabularInline):
    model = Owner.flat.through
    raw_id_fields = ('flat', )
    verbose_name = 'Связь с квартирами'


class FlatsInline(admin.TabularInline):
    model = Flat.owned_by.through
    raw_id_fields = ('owner', )
    verbose_name = 'Связь с людьми'

#
# class OwnerFlatAdmin(admin.ModelAdmin):
#     raw_id_fields = ('owner', 'flat')


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address']  # , 'owner__owner']
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ['new_building']
    list_filter = ('new_building',)
    raw_id_fields = ('liked_by',)
    inlines = [OwnersInline, ]


class OwnerAdmin(admin.ModelAdmin):
    search_fields = ['owner', 'flat__address', 'owner_pure_phone']
    raw_id_fields = ('flat',)
    list_display = ('owner', 'owner_pure_phone', 'get_flats')
    inlines = [OwnersInline, ]
    exclude = ('flat', )

    @staticmethod
    def get_flats(obj):
        return ", ".join([flat.__str__() for flat in obj.flat.all()])


class ClaimAdmin(admin.ModelAdmin):
    search_fields = ['username__username', 'flat__address']
    raw_id_fields = ('flat',)
    list_display = ('username', 'flat', 'claim_text')


admin.site.register(Flat, FlatAdmin)
admin.site.register(Claim, ClaimAdmin)
admin.site.register(Owner, OwnerAdmin)
