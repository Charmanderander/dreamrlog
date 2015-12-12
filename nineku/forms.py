from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class haikuForm(forms.Form):
    first_verse = forms.CharField(widget=forms.TextInput(attrs={'id':'box1','class' : 'form-control', 'placeholder':'First Verse', 'oninput':'count(this.value,1)'}), max_length=100)
    second_verse = forms.CharField(widget=forms.TextInput(attrs={'id':'box2','class' : 'form-control', 'placeholder':'Second Verse', 'oninput':'count(this.value,2)'}),max_length=100)
    third_verse = forms.CharField(widget=forms.TextInput(attrs={'id':'box3','class' : 'form-control', 'placeholder':'Third Verse', 'oninput':'count(this.value,3)'}),max_length=100)

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'E-mail address'}))
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

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
        raise forms.ValidationError('duplicate email')

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
    password = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Password', }),max_length=100)
