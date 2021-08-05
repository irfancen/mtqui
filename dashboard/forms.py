from django import forms
from django.forms.formsets import BaseFormSet

class EnrollmentForm(forms.Form):
    nama = forms.CharField(
                    max_length=100,
                    widget=forms.TextInput(attrs={
                        'placeholder' : 'Nama Peserta',
                    }),
                    required=False)
   
    jurusan = forms.CharField(
                    max_length=50,
                    widget=forms.TextInput(attrs={
                        'placeholder' : 'Jurusan',
                    }),
                    required=False)

    angkatan = forms.CharField(
                    max_length=4,
                    widget=forms.TextInput(attrs={
                        'placeholder' : 'Angkatan',
                    }),
                    required=False)

    no_hp = forms.CharField(
                    max_length=15,
                    widget=forms.TextInput(attrs={
                        'placeholder' : 'No. HP',
                    }),
                    required=False)

    line_id = forms.CharField(
                    max_length=30,
                    widget=forms.TextInput(attrs={
                        'placeholder' : 'ID Line',
                    }),
                    required=False)

    is_ketua = forms.BooleanField(required=False)

class EnrollmentListForm(forms.Form):
    nama = forms.CharField(
                    max_length=100,
                    widget=forms.TextInput(attrs={
                        'placeholder' : 'Nama Peserta',
                        'readonly' : True,
                    }),
                    required=False)

    fakultas = forms.CharField(
                    max_length=50,
                    widget=forms.TextInput(attrs={
                        'placeholder' : 'Fakultas',
                        'readonly' : True,
                    }),
                    required=False)
    
    jurusan = forms.CharField(
                    max_length=50,
                    widget=forms.TextInput(attrs={
                        'placeholder' : 'Jurusan',
                        'readonly' : True,
                    }),
                    required=False)

    angkatan = forms.CharField(
                    max_length=4,
                    widget=forms.TextInput(attrs={
                        'placeholder' : 'Angkatan',
                        'readonly' : True,
                    }),
                    required=False)

    no_hp = forms.CharField(
                    max_length=15,
                    widget=forms.TextInput(attrs={
                        'placeholder' : 'No. HP',
                        'readonly' : True,
                    }),
                    required=False)

    line_id = forms.CharField(
                    max_length=30,
                    widget=forms.TextInput(attrs={
                        'placeholder' : 'ID Line',
                        'readonly' : True,
                    }),
                    required=False)

    is_ketua = forms.BooleanField(
                    widget=forms.CheckboxInput(attrs={
                        'disabled' : True,
                    }),
                    required=False)

class BaseEnrollmentFormSet(BaseFormSet):
    def clean(self):
        if any(self.errors):
            return
        
        ketua_count = 0
        valid_count = 0

        for form in self.forms:
            if form.cleaned_data:
                nama = form.cleaned_data['nama']
                jurusan = form.cleaned_data['jurusan']
                angkatan = form.cleaned_data['angkatan']
                no_hp = form.cleaned_data['no_hp']
                line_id = form.cleaned_data['line_id']
                is_ketua = form.cleaned_data['is_ketua']

                if is_ketua:
                    ketua_count += 1

                if (nama or jurusan or angkatan or no_hp or line_id):
                    # Check missing fields
                    if not nama:
                        raise forms.ValidationError("Ada peserta dengan data Nama yang belum diisi", code="missing_nama")

                    if not jurusan:
                        raise forms.ValidationError("Ada peserta dengan data Jurusan yang belum diisi", code="missing_jurusan")

                    if not angkatan:
                        raise forms.ValidationError("Ada peserta dengan data Angkatan yang belum diisi", code="missing_angkatan")

                    if not no_hp:
                        raise forms.ValidationError("Ada peserta dengan data No. HP yang belum diisi", code="missing_no_hp")

                    if not line_id:
                        raise forms.ValidationError("Ada peserta dengan data ID Line yang belum diisi", code="missing_line_id")

                    # Check field and data validity
                    if not angkatan.isdigit():
                        raise forms.ValidationError("Ada data Angkatan yang tidak valid", code="invalid_angkatan")

                    if not no_hp.isdigit():
                        raise forms.ValidationError("Ada data No. HP yang tidak valid", code="invalid_no_hp")

                    valid_count += 1
        
        # Check team captain validity
        if valid_count > 0 and ketua_count == 0:
            raise forms.ValidationError("Masing-masing tim harus memiliki satu orang ketua", code="no_ketua")

        if valid_count > 0 and ketua_count > 1:
            raise forms.ValidationError("Masing-masing tim hanya diperbolehkan memiliki satu orang ketua", code="multiple_ketua")
