from django.shortcuts import render
from .models import Kegiatan, GalleryImage


def gallery(request):
    grand_opening_img = GalleryImage.objects.filter(kegiatan__name="Grand Opening")
    competition_img = GalleryImage.objects.filter(kegiatan__name="Competition")
    closing_ceremony_img = GalleryImage.objects.filter(kegiatan__name="Closing Ceremony")

    context = {
        'go_img': grand_opening_img,
        'comp_img': competition_img,
        'cc_img': closing_ceremony_img,
    }

    return render(request, 'gallery.html', context)
