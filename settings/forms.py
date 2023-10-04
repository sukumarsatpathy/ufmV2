from django import forms
from .models import WebSettings


class WebSettingsForm(forms.ModelForm):
    class Meta:
        model = WebSettings
        fields = ('title', 'slogan', 'logo_dark', 'logo_light', 'favicon', 'meta_title', 'meta_description',
                  'meta_keywords', 'default_user', 'public_key', 'private_key')

    def __init__(self, *args, **kwargs):
        super(WebSettingsForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['slogan'].widget.attrs['class'] = 'form-control'
        self.fields['logo_dark'].widget.attrs['class'] = 'form-control'
        self.fields['logo_light'].widget.attrs['class'] = 'form-control'
        self.fields['favicon'].widget.attrs['class'] = 'form-control'
        self.fields['meta_title'].widget.attrs['class'] = 'form-control kt_docs_maxlength_basic'
        self.fields['meta_title'].widget.attrs['maxlength'] = '60'
        self.fields['meta_description'].widget.attrs['class'] = 'form-control kt_docs_maxlength_basic'
        self.fields['meta_description'].widget.attrs['maxlength'] = '255'
        self.fields['meta_keywords'].widget.attrs['class'] = 'form-control'
        self.fields['default_user'].widget.attrs['class'] = 'form-control'
        self.fields['public_key'].widget.attrs['class'] = 'form-control'
        self.fields['private_key'].widget.attrs['class'] = 'form-control'
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = 'Provide Detail'