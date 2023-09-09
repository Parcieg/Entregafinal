from django import forms


class Loginform(forms.Form):
    usuario = forms.CharField(max_length=50)
    contrasena = forms.CharField(max_length=50, widget=forms.PasswordInput)


class Crearusuario(forms.Form):
    usuario = forms.CharField(max_length=50)
    correo = forms.EmailField()
    contrasena = forms.CharField(max_length=50, widget=forms.PasswordInput)
