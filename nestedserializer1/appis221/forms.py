from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit
from django import forms
from setuptools import sic

from .models import *
class NameWidget(forms.MultiWidget):
    def __init__(self,attrs=None):
        super().__init__(
            [
                forms.TextInput(),
                forms.TextInput()
            ],attrs)
    def decompress(self, value):
        if value:
            return value.split(' ')
        return ['','']
class Namefield(forms.MultiValueField):
    widget=NameWidget
    def __init__(self,*args,**kwargs):
        fields=(
            forms.CharField(),
            forms.CharField()
        )
        super().__init__(fields,*args,**kwargs)

    def compress(self,data_list):
        return f'{data_list[0]} {data_list[1]}'
class Contactforms(forms.Form):
    name=Namefield()
    email=forms.EmailField(label='E-mail')
    category=forms.ChoiceField(choices=[('questions','Questions'),('other','Other')])
    subject=forms.CharField(required=False)
    body=forms.CharField(widget=forms.Textarea)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper=FormHelper
        self.helper.form_method='post'

        self.helper.layout=Layout(
            'name',
            'email',
            'category',
            'subject',
            Submit('submit','Submit',css_class='btn-success')
        )

class Snippetform(forms.ModelForm):
    class Meta:
        model=snippet
        fields="__all__"

