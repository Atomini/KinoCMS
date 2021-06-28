from django.contrib.auth.forms import UserCreationForm
from adminka.models import User
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', "username", 'email', 'address', 'password1', 'password2', 'card_num',
                  'language', 'sex', 'phone', 'birth_date', 'city')


class UpdateUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', "username", 'email', 'address', 'card_num',
                  'language', 'sex', 'phone', 'birth_date', 'city')
