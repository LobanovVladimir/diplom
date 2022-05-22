from dataclasses import fields

from matplotlib import widgets
from .models import *
from django import forms

class UsersForm(forms.ModelForm):
    
    class Meta:
        model = users
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
        }
    def clean_name(self):
        print(self.cleaned_data)
        myname = self.cleaned_data['name']
        dbuser = users.objects.filter(name=myname)
        if dbuser.count() !=0:
            raise forms.ValidationError('Пользователь с таким именем уже существует')
        return self.cleaned_data['name']

    def clean_password(self):
        print(self.data)
        mypassword1 =self.cleaned_data['password'] 
        mypassword2 = self.data['password2']
        if mypassword1==mypassword2:
            return mypassword1
        raise forms.ValidationError('Пароли не совпадают!')

class  AUsersForm(forms.ModelForm):
    
    class Meta:
        model = users
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
        }
    def clean_name(self):
        print(self.cleaned_data)
        myname = self.cleaned_data['name']
        dbuser = users.objects.filter(name=myname)
        if dbuser.count() !=0:
            return self.cleaned_data['name']
        raise forms.ValidationError('Пользователя с таким именем не существует')

    def clean_password(self):
        print(self.data)
        mypassword1 =self.cleaned_data['password'] 
        dbuser = users.objects.get(name=self.data['name'])
        if mypassword1==dbuser.password:
            return mypassword1 
        raise forms.ValidationError('Пароль неверный!')

class SaveFile(forms.ModelForm):

    class Meta:
        model = places
        fields='__all__'
    
