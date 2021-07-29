from django import forms
from django.forms.formsets import BaseFormSet

class EnrollmentForm(forms.Form):
    nama = forms.CharField(
                    max_length=100,
                    widget=forms.TextInput(attrs={
                        'placeholder' : 'Nama Peserta',
                    }),
                    required=False)

    npm = forms.CharField(
                    max_length=10,
                    widget=forms.TextInput(attrs={
                        'placeholder' : 'NPM',
                    }),
                    required=False)

class BaseEnrollmentFormSet(BaseFormSet):
    def clean(self):
        if any(self.errors):
            return
        
        daftar_npm = []
        duplikat = False

        for form in self.forms:
            if form.cleaned_data:
                nama = form.cleaned_data['nama']
                npm = form.cleaned_data['npm']

                if npm.isdigit():
                    if npm in daftar_npm:
                        duplikat = True
                    daftar_npm.append(npm)

                if duplikat:
                    raise forms.ValidationError("Ada peserta dengan NPM yang sama", code='npm_duplikat')

                if nama and not npm:
                    raise forms.ValidationError("Ada peserta yang belum dicantumkan NPM-nya", code="missing_npm")
                
                if npm and not nama:
                    raise forms.ValidationError("Ada peserta yang belum dicantumkan Nama-nya", code="missing_nama")
