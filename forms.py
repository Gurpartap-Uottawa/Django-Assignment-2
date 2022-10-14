# import the standard Django Forms
# from built-in library
from django import forms
from .models import projectModel
   
# creating a form 
class InputForm(forms.ModelForm):
    class Meta:
        model = projectModel
        fields = "__all__"