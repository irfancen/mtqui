from django import forms
from django.forms.formsets import BaseFormSet
import magic

class PesertaForm(forms.Form):
    def __init__(self, *args, **kwargs):
        edit_form = kwargs.pop("edit_form", False)
        super(PesertaForm, self).__init__(*args, **kwargs)

        if edit_form:
            self.fields['foto_ktm'].required = False
            self.fields['screenshot_siak'].required = False

    nama = forms.CharField(
                max_length=100, 
                widget=forms.TextInput(attrs={
                    'class' : 'form-control',
                }))

    jurusan = forms.CharField(
                max_length=50, 
                widget=forms.TextInput(attrs={
                    'class' : 'form-control',
                }))

    angkatan = forms.CharField(
                max_length=4, 
                widget=forms.TextInput(attrs={
                    'class' : 'form-control',
                }))

    no_hp = forms.CharField(
                max_length=15, 
                widget=forms.TextInput(attrs={
                    'class' : 'form-control',
                }))

    line_id = forms.CharField(
                max_length=30, 
                widget=forms.TextInput(attrs={
                    'class' : 'form-control',
                }))

    foto_ktm = forms.ImageField(
                widget=forms.FileInput(attrs={
                    'class' : 'form-control-file',
                }))

    screenshot_siak = forms.ImageField(
                widget=forms.FileInput(attrs={
                    'class' : 'form-control-file',
                }))

    def clean_angkatan(self):
        angkatan = self.cleaned_data['angkatan']
        if not angkatan.isdigit():
            raise forms.ValidationError("Data Angkatan harus bernilai angka", code="invalid_angkatan")
        return angkatan

    def clean_no_hp(self):
        no_hp = self.cleaned_data['no_hp']
        if not no_hp.isdigit():
            raise forms.ValidationError("Data No. HP harus bernilai angka", code="invalid_no_hp")
        return no_hp

    def clean_foto_ktm(self):
        foto_ktm = self.cleaned_data.get("foto_ktm")
        if foto_ktm and foto_ktm.size > 5242880: # 5 MB
            raise forms.ValidationError("Ukuran file Foto KTM terlalu besar (maksimal 5 MB)", code="large_foto_ktm")
        return foto_ktm

    def clean_screenshot_siak(self):
        screenshot_siak = self.cleaned_data.get("screenshot_siak")
        if screenshot_siak and screenshot_siak.size > 5242880: # 5 MB
            raise forms.ValidationError("Ukuran file Screenshot SIAK terlalu besar (maksimal 5 MB)", code="large_screenshot_siak")
        return screenshot_siak


class KelompokForm(forms.Form):
    nama = forms.CharField(
                max_length=100, 
                widget=forms.TextInput(attrs={
                    'class' : 'form-control',
                }))


class AnggotaForm(forms.Form):
    def __init__(self, *args, **kwargs):
        edit_form = kwargs.pop("edit_form", False)
        super(AnggotaForm, self).__init__(*args, **kwargs)

        if edit_form:
            self.fields['foto_ktm'].required = False
            self.fields['screenshot_siak'].required = False

    nama = forms.CharField(
                max_length=100, 
                widget=forms.TextInput(attrs={
                    'class' : 'form-control',
                }))

    jurusan = forms.CharField(
                max_length=50, 
                widget=forms.TextInput(attrs={
                    'class' : 'form-control',
                }))

    angkatan = forms.CharField(
                max_length=4, 
                widget=forms.TextInput(attrs={
                    'class' : 'form-control',
                }))

    no_hp = forms.CharField(
                max_length=15, 
                widget=forms.TextInput(attrs={
                    'class' : 'form-control',
                }))

    line_id = forms.CharField(
                max_length=30, 
                widget=forms.TextInput(attrs={
                    'class' : 'form-control',
                }))

    foto_ktm = forms.ImageField(
                widget=forms.FileInput(attrs={
                    'class' : 'form-control-file',
                }))

    screenshot_siak = forms.ImageField(
                widget=forms.FileInput(attrs={
                    'class' : 'form-control-file',
                }))

    def clean_angkatan(self):
        angkatan = self.cleaned_data['angkatan']
        if not angkatan.isdigit():
            raise forms.ValidationError("Data Angkatan harus bernilai angka", code="invalid_angkatan")
        return angkatan

    def clean_no_hp(self):
        no_hp = self.cleaned_data['no_hp']
        if not no_hp.isdigit():
            raise forms.ValidationError("Data No. HP harus bernilai angka", code="invalid_no_hp")
        return no_hp

    def clean_foto_ktm(self):
        foto_ktm = self.cleaned_data.get("foto_ktm")
        if foto_ktm and foto_ktm.size > 5242880: # 5 MB
            raise forms.ValidationError("Ukuran file Foto KTM terlalu besar (maksimal 5 MB)", code="large_foto_ktm")
        return foto_ktm

    def clean_screenshot_siak(self):
        screenshot_siak = self.cleaned_data.get("screenshot_siak")
        if screenshot_siak and screenshot_siak.size > 5242880: # 5 MB
            raise forms.ValidationError("Ukuran file Screenshot SIAK terlalu besar (maksimal 5 MB)", code="large_screenshot_siak")
        return screenshot_siak


class AnggotaDAQForm(forms.Form):
    def __init__(self, *args, **kwargs):
        edit_form = kwargs.pop("edit_form", False)
        super(AnggotaDAQForm, self).__init__(*args, **kwargs)

        if edit_form:
            self.fields['foto_ktm'].required = False
            self.fields['screenshot_siak'].required = False
            self.fields['file_cv'].required = False

    nama = forms.CharField(
                max_length=100, 
                widget=forms.TextInput(attrs={
                    'class' : 'form-control',
                }))

    jurusan = forms.CharField(
                max_length=50, 
                widget=forms.TextInput(attrs={
                    'class' : 'form-control',
                }))

    angkatan = forms.CharField(
                max_length=4, 
                widget=forms.TextInput(attrs={
                    'class' : 'form-control',
                }))

    no_hp = forms.CharField(
                max_length=15, 
                widget=forms.TextInput(attrs={
                    'class' : 'form-control',
                }))

    line_id = forms.CharField(
                max_length=30, 
                widget=forms.TextInput(attrs={
                    'class' : 'form-control',
                }))

    is_ketua = forms.BooleanField(
                required=False,
                widget=forms.CheckboxInput(attrs={
                    'class' : 'form-check-input checkbox',
                }))

    foto_ktm = forms.ImageField(
                widget=forms.FileInput(attrs={
                    'class' : 'form-control-file',
                }))

    screenshot_siak = forms.ImageField(
                widget=forms.FileInput(attrs={
                    'class' : 'form-control-file',
                }))

    file_cv = forms.FileField(
                widget=forms.FileInput(attrs={
                    'class' : 'form-control-file',
                }))

    def clean_angkatan(self):
        angkatan = self.cleaned_data['angkatan']
        if not angkatan.isdigit():
            raise forms.ValidationError("Data Angkatan harus bernilai angka", code="invalid_angkatan")
        return angkatan

    def clean_no_hp(self):
        no_hp = self.cleaned_data['no_hp']
        if not no_hp.isdigit():
            raise forms.ValidationError("Data No. HP harus bernilai angka", code="invalid_no_hp")
        return no_hp

    def clean_foto_ktm(self):
        foto_ktm = self.cleaned_data.get("foto_ktm")
        if foto_ktm and foto_ktm.size > 5242880: # 5 MB
            raise forms.ValidationError("Ukuran file Foto KTM terlalu besar (maksimal 5 MB)", code="large_foto_ktm")
        return foto_ktm

    def clean_screenshot_siak(self):
        screenshot_siak = self.cleaned_data.get("screenshot_siak")
        if screenshot_siak and screenshot_siak.size > 5242880: # 5 MB
            raise forms.ValidationError("Ukuran file Screenshot SIAK terlalu besar (maksimal 5 MB)", code="large_screenshot_siak")
        return screenshot_siak
    
    def clean_file_cv(self):
        file_cv = self.cleaned_data.get("file_cv")
        if file_cv:
            filetype = magic.from_buffer(file_cv.read(), mime=True)
            if filetype != "application/pdf":
                raise forms.ValidationError("Berkas CV harus dalam format PDF", code="invalid_format_file_cv")
            if file_cv.size > 20971520: # 20 MB
                raise forms.ValidationError("Ukuran berkas CV terlalu besar (maksimal 20 MB)", code="large_file_cv")
        return file_cv


class EditKelompokDAQForm(forms.Form):
    def __init__(self, *args, **kwargs):
        ketua_choices = kwargs.pop("ketua_choices", None)
        super(EditKelompokDAQForm, self).__init__(*args, **kwargs)
        self.fields['ketua'].choices = ketua_choices

    nama = forms.CharField(
                max_length=100, 
                widget=forms.TextInput(attrs={
                    'class' : 'form-control',
                }))

    ketua = forms.ChoiceField(
                widget=forms.Select(attrs={
                    'class' : 'form-control',
                }))


class BaseAnggotaDAQFormSet(BaseFormSet):
    def clean(self):
        if any(self.errors):
            return
        
        ketua_count = 0
        valid_count = 0

        for form in self.forms:
            is_ketua = form.cleaned_data.get("is_ketua")
            if is_ketua:
                ketua_count += 1
            valid_count += 1
        
        if valid_count > 0 and ketua_count == 0:
            raise forms.ValidationError("Masing-masing tim harus memiliki satu orang ketua", code="no_ketua")

        if valid_count > 0 and ketua_count > 1:
            raise forms.ValidationError("Masing-masing tim hanya diperbolehkan memiliki satu orang ketua", code="multiple_ketua")
