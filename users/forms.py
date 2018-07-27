from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from bootstrap3_datetime.widgets import DateTimePicker
from .models import UserProfile


class UserCreatForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserCreatForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs={'class':'form-control'}

        self.fields['password'].widget=forms.PasswordInput(attrs={'class':'form-control'})

    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username',  'email', 'password']

    def clean_email(self):          #email önceden kullanılmış mı?
        email = self.cleaned_data['email']
        uzunluk = len(User.objects.filter(email=email))
        if uzunluk>0:
            raise forms.ValidationError('Bu email adresi önceden kullanılmış')
        return email


class UserProfileEdit(forms.ModelForm):
    ERKEK = 'E'
    KIZ = 'K'
    OTHER = 'O'
    CINSIYET = ((ERKEK, 'Erkek'), (KIZ, 'Kadın'), (OTHER, 'Other'))

    cinsiyet=forms.CharField(widget=forms.Select(choices=CINSIYET))
    dogum = forms.DateField(input_formats=['%d/%m/%Y'], widget=DateTimePicker(options={'viewMode':'years', "format": "DD/MM/YYYY","pickTime": False}))
    telefon_numarasi=forms.CharField(max_length=11, label='Telefon Numarası', required=False)


    class Meta:
        model = User
        fields=['username', 'first_name', 'last_name', 'email', 'dogum', 'cinsiyet', 'telefon_numarasi']

    def __init__(self, *args, **kwargs):
        super(UserProfileEdit, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs={'class':'form-control'}

class UserPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordChangeForm, self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class':'form-control'}

class LoginForm(forms.Form):        #neden form modelform değil
    username=forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean_username(self):
        username = self.cleaned_data['username']

        if '@' in username:
            user = User.objects.filter(email=username)
            if len(user) == 1:
                user = user.first()
                return user.username
            else:
                raise forms.ValidationError('Böyle bir kullanıcı bulunamadı!')

        return username


class UserListForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class UserUploadPhotoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profil_photo']
