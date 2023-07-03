from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Profile


class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              }))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                widget=forms.TextInput(attrs={ 'required': False,
                                                               'class': 'form-control',
                                                              }))

    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    address_city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    address_state = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    address_pin = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    address_locality = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'required': False}))
    registration_year = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    passing_out_year = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'required': False}))
    department = forms.ChoiceField(choices=Profile.DEPARTMENTS, widget=forms.Select(attrs={'class': 'form-control'}))
    contact_self = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    contact_parents = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'required': False}))
    user_type = forms.ChoiceField(choices=Profile.USER_TYPES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'address_city', 'address_state', 'address_pin', 'address_locality', 'registration_year', 'passing_out_year', 'department', 'contact_self', 'contact_parents', 'user_type']


