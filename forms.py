from django import forms
from django.forms import CharField, DecimalField
from django.forms import TextInput
from .models import AdCard

class FindFormMain(forms.Form):
    text_to_find = forms.CharField(label='', required=False)

class AuthForm(forms.Form):
    username = CharField(label = 'Логин')
    password = CharField(label='Пароль', widget=forms.PasswordInput())
    firstname = CharField(label = 'Имя')
    secondname = CharField(label = 'Отчество', required=False)
    surname = CharField(label = 'Фамилия', required=False)
    phone = CharField(label = 'Телефон', required=False)
    email = CharField(label = 'E-mail', required=False)

class UploadPicture(forms.Form):
    file = forms.ImageField(label="")

class EditAdCard(forms.ModelForm):
    class Meta:
        model = AdCard
        fields = ['name', 'decription', 'price', 'category_id', 'is_active', 'published', 'type_id']