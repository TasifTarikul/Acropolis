from django.forms import ModelForm
from userProfileApp.models import AcropolisModel, SarawakModel, VisaModel
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.conf import settings
from django.contrib.auth import get_user_model
from coreApp.models import User
from django import forms


class AcropolisForm(ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(), max_length=100, null=True, blank=True)
    last_name = forms.CharField(widget=forms.TextInput(), max_length=100, null=True, blank=True)

    class Meta:
        model = AcropolisModel
        fields = '__all__'
        exclude = ['user_profile', ]

    def __init__(self, *args, **kwargs):

        super(AcropolisForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].initial = kwargs['instance'].user_profile.first_name
        self.fields['last_name'].initial = kwargs['instance'].user_profile.last_name

    def save(self, commit=True):
        super(AcropolisForm, self).save()

        self.user_profile.first_name = self.cleaned_data.get('first_name')
        self.user_profile.last_name = self.cleaned_data.get('last_name')
        self.save()


class SarawakForm(ModelForm):
    class Meta:
        model = SarawakModel
        fields = '__all__'


class VisaForm(ModelForm):
    class Meta:
        model = VisaModel
        fields = '__all__'


class UserSignUpForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'password1', 'password2']


