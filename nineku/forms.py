from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'E-mail address','class' : 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First name', 'class' : 'form-control'}),required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' Last name', 'class' : 'form-control'}),required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username (Will be visible when you post)', 'class' : 'form-control'}),required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class' : 'form-control'}),required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password again', 'class' : 'form-control'}),required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

    #clean email field
    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User._default_manager.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('The email provided is already is use')

    #modify save() method so that we can set user.is_active to False when we first create our user
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.is_active = False # not active until he opens activation link
            user.save()

        return user


class loginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Username', }), max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder':'Password', }),max_length=100)


class dreamForm(forms.Form):
    dream = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control', 'placeholder':'Enter your dream here', 'oninput':'checkBoxes()','id':'textArea' }), max_length=3000)
    mood = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Describe your mood',  'oninput':'checkBoxes()','id':'mood'  }), max_length=100)
    tags = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Tags',  'oninput':'checkBoxes()','id':'tags' }), max_length=100)
