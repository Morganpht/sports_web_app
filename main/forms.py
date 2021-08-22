import datetime
from typing import NewType
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class NewUserForm(UserCreationForm):

    years = []
    for i in reversed(range((datetime.date.today().year)-120, (datetime.date.today().year)+1)):
        years.append(i)

    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    date_of_birth = forms.DateField(required=True, widget=forms.SelectDateWidget(years=years))
    gender = forms.ChoiceField(required=True, choices=Profile.genderChoices, widget=forms.Select())
    class Meta:
        model = User
        fields = (
            "username", 
            "email", 
            "first_name", 
            "last_name", 
            "date_of_birth",
            "gender",
            "password1", 
            "password2",
            )

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.second_name = self.cleaned_data['last_name']
        user.date_of_birth = self.cleaned_data['date_of_birth']
        user.gender = self.cleaned_data['gender']
        if commit:
            user.save()
        return user


'''class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('teams',)''' #this is the many to many relations ship from models.py