from .models import Account
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label='email', widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Account
        fields = ('email', 'password', 'username')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            username = self.cleaned_data['username']
            if not authenticate(email=email, password=password, username=username):
                raise forms.ValidationError("Invalid login!")


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Account
        fields = ('username','email', 'password1', 'password2', 'phone_number')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            email_in_use = Account.objects.exclude(pk = self.instance.pk).get(email=email)
        except Account.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % email_in_use)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            username_in_use = Account.objects.exclude(pk = self.instance.pk).get(username=username)
        except Account.DoesNotExist:
            return username
        raise forms.ValidationError('Username "%s" is already in use.' % username_in_use)


class EditProfileForm(forms.ModelForm):
    profile_image = forms.ImageField(widget=forms.FileInput)
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'profile_image', 'address')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            email_in_use = Account.objects.exclude(pk = self.instance.pk).get(email=email)
        except Account.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % email_in_use)

