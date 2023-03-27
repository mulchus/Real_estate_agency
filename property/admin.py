from django.contrib import admin

from .models import Flat
from .models import Claim
from .models import Owner


class OwnersInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ('flat', 'owner')
    verbose_name = 'Связь с квартирами'


class FlatsInline(admin.TabularInline):
    model = Flat.owner_by.through
    raw_id_fields = ('flat', 'owner')
    verbose_name = 'Связь с людьми'


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address']
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ['new_building']
    list_filter = ('new_building',)
    raw_id_fields = ('liked_by', )
    inlines = [FlatsInline, ]


class OwnerAdmin(admin.ModelAdmin):
    search_fields = ['name', 'flat__address', 'pure_phonenumber']
    raw_id_fields = ('flats',)
    list_display = ('name', 'pure_phonenumber', 'get_flats')
    inlines = [OwnersInline, ]

    @staticmethod
    def get_flats(obj):
        return ", ".join([flat.__str__() for flat in obj.flats.all()])


class ClaimAdmin(admin.ModelAdmin):
    search_fields = ['username__username', 'flat__address']
    raw_id_fields = ('flat',)
    list_display = ('username', 'flat', 'claim_text')


admin.site.register(Flat, FlatAdmin)
admin.site.register(Claim, ClaimAdmin)
admin.site.register(Owner, OwnerAdmin)
