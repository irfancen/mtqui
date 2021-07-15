from dashboard.models import MetadataFakultas
from django.contrib import admin

# Register your models here.
class MetadataFakultasPanelConfig(admin.ModelAdmin):
    search_fields = ("username_fakultas__username", "nama_fakultas", "singkatan_fakultas")
    ordering = ("nama_fakultas",)
    list_display = ("nama_fakultas", "username_fakultas")

admin.site.register(MetadataFakultas, MetadataFakultasPanelConfig)
