from django import forms
from .models import Account, Address


class LoginForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['email', 'password']

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['placeholder'] = 'Provide Details'


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'form-control',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password'
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'password']

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Password does not match!")

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['placeholder'] = 'Provide Details'


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'status')

    def __init__(self, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['phone_number'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['class'] = 'form-select'
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = 'Provide Details'


class AccountAddForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'class': 'form-control',
            }
        ),
        label="Password", # Explicitly set the label
        error_messages={'required': 'Password is required.'}
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirm Password',
                'class': 'form-control',
            }
        ),
        label="Confirm Password",  # Explicitly set the label
        error_messages={'required': 'Confirm password is required.'}
    )

    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'status')

    def clean(self):
        cleaned_data = super(AccountAddForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Password does not match!")

    def __init__(self, *args, **kwargs):
        super(AccountAddForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['phone_number'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['class'] = 'form-select'
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = 'Provide Details'

        for field_name, field in self.fields.items():
            field.error_messages['required'] = f'{field.label} is required.'


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('address_line_1', 'address_line_2', 'city', 'state', 'country', 'postal_code')

    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = 'Provide Detail'
            self.fields[field].widget.attrs['class'] = 'form-control'

        for field_name, field in self.fields.items():
            field.error_messages['required'] = f'{field.label} is required.'