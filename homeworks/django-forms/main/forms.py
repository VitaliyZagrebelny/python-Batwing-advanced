from django import forms
from django.contrib.auth.models import User


class UserSingUp(forms.ModelForm):
    def save(self, commit=True):
        instance = super(UserSingUp, self).save(commit=False)
        instance.is_superuser = False
        instance.is_staff = False
        instance.is_active = True
        if commit:
            instance.save()
        return instance

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password"]


class UserSingIn(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clear_user(self):
        username = self.cleaned_data.get("username")
        get_user = User.objects.filter(username_iexact=username)
        if not get_user:
            raise forms.ValidationError("There is no user.")
        return username
