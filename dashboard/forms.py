from django import forms
from django.forms.formsets import BaseFormSet
import magic

class PesertaForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(PesertaForm, self).__init__(*args, **kwargs)

        if kwargs.pop("edit_form", False):
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
        super(AnggotaForm, self).__init__(*args, **kwargs)

        if kwargs.pop("edit_form", False):
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
        super(AnggotaDAQForm, self).__init__(*args, **kwargs)

        if kwargs.pop("edit_form", False):
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
    def __init__(self, ketua_choices, *args, **kwargs):
        super(EditKelompokDAQForm, self).__init__(*args, **kwargs)
        self.fields['ketua'].choices = ketua_choices

    nama = forms.CharField(
                max_length=100, 
                widget=forms.TextInput(attrs={
                    'class' : '',
                }))

    ketua = forms.ChoiceField(
                widget=forms.Select(attrs={
                    'class' : '',
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











# class EnrollmentForm(forms.Form):
#     nama = forms.CharField(
#                     max_length=100,
#                     widget=forms.TextInput(attrs={

#                         'placeholder' : 'Nama Peserta',
#                         'class' : 'form-input-field',
#                     }),
#                     required=False)
   
#     jurusan = forms.CharField(
#                     max_length=50,
#                     widget=forms.TextInput(attrs={
#                         'placeholder' : 'Jurusan',
#                         'class' : 'form-input-field',
#                     }),
#                     required=False)

#     angkatan = forms.CharField(
#                     max_length=4,
#                     widget=forms.TextInput(attrs={
#                         'placeholder' : 'Angkatan',
#                         'class' : 'form-input-field',
#                     }),
#                     required=False)

#     no_hp = forms.CharField(
#                     max_length=15,
#                     widget=forms.TextInput(attrs={
#                         'placeholder' : 'No. HP',
#                         'class' : 'form-input-field',
#                     }),
#                     required=False)

#     line_id = forms.CharField(
#                     max_length=30,
#                     widget=forms.TextInput(attrs={
#                         'placeholder' : 'ID Line',
#                         'class' : 'form-input-field',
#                     }),
#                     required=False)

#     foto_ktm = forms.ImageField(required=False)

#     screenshot_siak = forms.ImageField(required=False)

#     file_cv = forms.FileField(required=False)

#     is_ketua = forms.BooleanField(
#                     widget=forms.CheckboxInput(attrs={
#                         'class' : 'checkbox',
#                     }),
#                     required=False)

# class EnrollmentListForm(forms.Form):
#     nama = forms.CharField(
#                     max_length=100,
#                     widget=forms.TextInput(attrs={
#                         'placeholder' : 'Nama Peserta',
#                         'readonly' : True,
#                         'class' : 'form-input-field',
#                     }),
#                     required=False)

#     fakultas = forms.CharField(
#                     max_length=50,
#                     widget=forms.TextInput(attrs={
#                         'placeholder' : 'Fakultas',
#                         'readonly' : True,
#                         'class' : 'form-input-field',
#                     }),
#                     required=False)
    
#     jurusan = forms.CharField(
#                     max_length=50,
#                     widget=forms.TextInput(attrs={
#                         'placeholder' : 'Jurusan',
#                         'readonly' : True,
#                         'class' : 'form-input-field',
#                     }),
#                     required=False)

#     angkatan = forms.CharField(
#                     max_length=4,
#                     widget=forms.TextInput(attrs={
#                         'placeholder' : 'Angkatan',
#                         'readonly' : True,
#                         'class' : 'form-input-field',
#                     }),
#                     required=False)

#     no_hp = forms.CharField(
#                     max_length=15,
#                     widget=forms.TextInput(attrs={
#                         'placeholder' : 'No. HP',
#                         'readonly' : True,
#                         'class' : 'form-input-field',
#                     }),
#                     required=False)

#     line_id = forms.CharField(
#                     max_length=30,
#                     widget=forms.TextInput(attrs={
#                         'placeholder' : 'ID Line',
#                         'readonly' : True,
#                         'class' : 'form-input-field',
#                     }),
#                     required=False)

#     is_ketua = forms.BooleanField(
#                     widget=forms.CheckboxInput(attrs={
#                         'disabled' : True,
#                         'class' : 'checkbox',
#                     }),
#                     required=False)

# class BaseEnrollmentFormSet(BaseFormSet):
#     def clean(self):
#         if any(self.errors):
#             return
        
#         ketua_count = 0
#         valid_count = 0

#         for form in self.forms:
#             if form.cleaned_data:
#                 nama = form.cleaned_data['nama']
#                 jurusan = form.cleaned_data['jurusan']
#                 angkatan = form.cleaned_data['angkatan']
#                 no_hp = form.cleaned_data['no_hp']
#                 line_id = form.cleaned_data['line_id']
#                 is_ketua = form.cleaned_data['is_ketua']

#                 if is_ketua:
#                     ketua_count += 1

#                 if (nama or jurusan or angkatan or no_hp or line_id):
#                     # Check missing fields
#                     if not nama:
#                         raise forms.ValidationError("Ada peserta dengan data Nama yang belum diisi", code="missing_nama")

#                     if not jurusan:
#                         raise forms.ValidationError("Ada peserta dengan data Jurusan yang belum diisi", code="missing_jurusan")

#                     if not angkatan:
#                         raise forms.ValidationError("Ada peserta dengan data Angkatan yang belum diisi", code="missing_angkatan")

#                     if not no_hp:
#                         raise forms.ValidationError("Ada peserta dengan data No. HP yang belum diisi", code="missing_no_hp")

#                     if not line_id:
#                         raise forms.ValidationError("Ada peserta dengan data ID Line yang belum diisi", code="missing_line_id")

#                     # Check field and data validity
#                     if not angkatan.isdigit():
#                         raise forms.ValidationError("Ada data Angkatan yang tidak valid", code="invalid_angkatan")

#                     if not no_hp.isdigit():
#                         raise forms.ValidationError("Ada data No. HP yang tidak valid", code="invalid_no_hp")

#                     valid_count += 1
        
#         # Check team captain validity
#         if valid_count > 0 and ketua_count == 0:
#             raise forms.ValidationError("Masing-masing tim harus memiliki satu orang ketua", code="no_ketua")

#         if valid_count > 0 and ketua_count > 1:
#             raise forms.ValidationError("Masing-masing tim hanya diperbolehkan memiliki satu orang ketua", code="multiple_ketua")
