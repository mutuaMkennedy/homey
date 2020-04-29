from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from leaflet.forms.widgets import LeafletWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class profile_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


    def signup(self,request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.save()
        # profile = UserProfile()
        # profile.user = user
        # profile.first_name = self.cleaned_data['first_name']
        # profile.last_name = self.cleaned_data['last_name']
        # profile.save()


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name','email']

class ProfileEditForm(forms.ModelForm):
    about = forms.CharField(widget=CKEditorUploadingWidget(config_name='user_profile'))
    class Meta:
        model = UserProfile
        exclude = ['user','account_type']
        fields = '__all__'
        widgets = {'location':LeafletWidget()}
