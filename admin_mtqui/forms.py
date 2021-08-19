from dashboard.models import TipeKompetisi
from django import forms

class KompetisiForm(forms.Form):
    def __init__(self, *args, **kwargs):
        tipe_choices = kwargs.pop("tipe_choices", None)
        super(KompetisiForm, self).__init__(*args, **kwargs)
        self.fields['tipe'].choices = tipe_choices

    judul = forms.CharField(max_length=100)

    kuota = forms.IntegerField()

    deadline_pendaftaran = forms.DateField(widget=forms.DateInput(
        attrs = {
            'type' : 'date',
            'required': True,
    }))

    tipe = forms.ChoiceField()

    kapasitas_kelompok = forms.IntegerField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        tipe = TipeKompetisi.objects.get(id=cleaned_data.get("tipe"))
        kapasitas_kelompok = cleaned_data.get("kapasitas_kelompok")

        if (str(tipe) != "Individu") and (kapasitas_kelompok is None):
            raise forms.ValidationError("Kapasitas kelompok harus diisi untuk tipe kompetisi Kelompok dan DAQ", code="missing_kapasitas_kelompok")
            