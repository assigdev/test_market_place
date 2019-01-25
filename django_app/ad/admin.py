from django.contrib import admin
from ad.models import Ad


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'user')
    raw_id_fields = ('city',)
