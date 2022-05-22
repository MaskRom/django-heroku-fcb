from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class ShortcutURLform(forms.ModelForm):
    class Meta:
        model = ShortcutURL
        fields = ['name', 'url']

class Infoform(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['posted_name', 'head', 'body']

class Timetableform(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = [f"{n}_{t}st{s}" for n in ["mon","tue", "wed", "thu", "fri"] for t in "123" for s in ["", "_sub"]]
