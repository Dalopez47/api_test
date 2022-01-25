from django.forms import ModelForm, EmailInput

from users.models import User


class PersonaForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }