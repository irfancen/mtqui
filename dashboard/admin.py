from dashboard.models import *
from django.contrib import admin

# Register your models here.
@admin.register(MetadataFakultas)
class MetadataFakultasPanelConfig(admin.ModelAdmin):
    search_fields = ("username_fakultas__username", "nama_fakultas", "singkatan_fakultas")
    ordering = ("nama_fakultas",)
    list_display = ("nama_fakultas", "username_fakultas")

@admin.register(TipeKompetisi)
class TipeKompetisiPanelConfig(admin.ModelAdmin):
    search_fields = ("tipe",)
    ordering = ("tipe",)
    list_display = ("tipe",)

@admin.register(Kompetisi)
class KompetisiPanelConfig(admin.ModelAdmin):
    search_fields = ("judul", "fakultas__username")
    ordering = ("judul", "fakultas__username", "tipe__tipe", "deadline_pendaftaran")
    list_display = ("judul", "fakultas", "tipe", "deadline_pendaftaran")
    list_filter = ("judul", "fakultas__username", "tipe__tipe")

@admin.register(Kelompok)
class KelompokPanelConfig(admin.ModelAdmin):
    search_fields = ("nama", "kompetisi__judul", "kompetisi__fakultas__username")
    ordering = ("nama", "kompetisi")
    list_display = ("nama", "kompetisi")
    list_filter = ("kompetisi",)

@admin.register(Peserta)
class PesertaPanelConfig(admin.ModelAdmin):
    search_fields = ("nama", "fakultas", "kompetisi__judul", "kompetisi__fakultas__username")
    ordering = ("nama", "kompetisi")
    list_display = ("nama", "kompetisi", "fakultas")
    list_filter = ("fakultas", "kompetisi")
