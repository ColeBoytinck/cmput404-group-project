from django import forms
from .models import Node
from django.contrib.auth.password_validation import validate_password


class ForeignServerRegisterForm(forms.ModelForm):

    foreign_server_hostname = forms.URLField(
        label="foreign_server_hostname", required=True)

    foreign_server_password = forms.CharField(
        label="foreign_server_password", max_length=30, required=True, widget=forms.PasswordInput, validators=[validate_password])

    hostname_registered_on_foreign_server = forms.URLField(
        label="hostname_registered_on_foreign_server", required=False, help_text="optional"
    )
    password_registered_on_foreign_server = forms.CharField(
        label="password_registered_on_foreign_server", max_length=30, required=False, help_text="optional", widget=forms.PasswordInput)

    image_share = forms.BooleanField(
        label="image_share", required=False, widget=forms.CheckboxInput)

    post_share = forms.BooleanField(
        label="post_share", required=False, widget=forms.CheckboxInput)

    class Meta:
        model = Node
        fields = ['foreign_server_hostname', 'foreign_server_password', 'hostname_registered_on_foreign_server',
                  'password_registered_on_foreign_server', 'image_share', 'post_share']
