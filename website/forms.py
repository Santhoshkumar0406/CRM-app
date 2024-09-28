from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Record

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='', widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Email'}))
    first_name = forms.CharField(label='', max_length=50, widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'First_name'}))
    last_name = forms.CharField(label='', max_length=50, widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last_name'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	


class addrecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, label='', max_length=50, widget = forms.widgets.TextInput(attrs={'class':'form-control', 'placeholder':'First_name'}))
    last_name = forms.CharField(required=True, label='', max_length=50, widget = forms.widgets.TextInput(attrs={'class':'form-control', 'placeholder':'Last_name'}))
    email = forms.EmailField(required=True, label='', widget = forms.widgets.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Email'}))
    phone = forms.CharField(required=True, label='', max_length=50, widget = forms.widgets.TextInput(attrs={'class':'form-control', 'placeholder':'phone'}))
    address = forms.CharField(required=True, label='', max_length=100, widget = forms.widgets.TextInput(attrs={'class':'form-control', 'placeholder':'address'}))
    city = forms.CharField(required=True, label='', max_length=50, widget = forms.widgets.TextInput(attrs={'class':'form-control', 'placeholder':'city'}))
    state = forms.CharField(required=True, label='', max_length=50, widget = forms.widgets.TextInput(attrs={'class':'form-control', 'placeholder':'state'}))
    zipcode = forms.CharField(required=True, label='', max_length=50, widget = forms.widgets.TextInput(attrs={'class':'form-control', 'placeholder':'zipcode'}))

    class Meta:
        model = Record
        exclude = ('user',)