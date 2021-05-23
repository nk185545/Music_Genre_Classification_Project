from django import forms
class MusicForm(forms.Form):
    file  = forms.FileField() # for creating file input