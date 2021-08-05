from dashboard.models import *
from django.contrib import admin

# Register your models here.
@admin.register(MetadataFakultas)
class MetadataFakultasPanelConfig(admin.ModelAdmin):
    search_fields = ("username_fakultas__username", "nama_fakultas", "singkatan_fakultas")
    ordering = ("nama_fakultas",)
    list_display = ("nama_fakultas", "username_fakultas")

@admin.register(Kompetisi)
class KompetisiPanelConfig(admin.ModelAdmin):
    search_fields = ("judul", "fakultas__username")
    ordering = ("judul", "fakultas__username", "deadline_pendaftaran")
    list_display = ("judul", "fakultas", "deadline_pendaftaran")
    list_filter = ("fakultas__username",)

@admin.register(Peserta)
class PesertaPanelConfig(admin.ModelAdmin):
    search_fields = ("nama", "fakultas", "kompetisi__judul", "kompetisi__fakultas__username")
    ordering = ("nama", "kompetisi")
    list_display = ("nama", "kompetisi", "fakultas")
    list_filter = ("fakultas", "kompetisi")
