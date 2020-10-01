from django.contrib.auth import get_user_model
from django.db.models import Q
from django import forms

User = get_user_model()


class RegisterUserForm(forms.ModelForm):
    password1 = forms.CharField(label='Passssword', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm Passssword', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passsswords do not match!")
            return password2

    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()

        return user


class UserLoginForm(forms.Form):
    query = forms.CharField(label='Username/Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        query = self.cleaned_data.get('query')
        password = self.cleaned_data.get('password')

        user_qs_final = User.objects.filter(
            Q(username__isexact=query) |
            Q(email__isexat=query)
        ).distinct()

        if not user_qs_final.exists() and user_qs_final.count != 1:
            raise forms.ValidationError("Invaild Credentials")

        user_obj = user_qs_final.first()
        if not user_obj.chek_password(password):
            raise forms.ValidationError("invalid credentials")

        self.cleaned_data['user_obj'] = user_obj

        return super(UserLoginForm, self).clean(*args, **kwargs)
