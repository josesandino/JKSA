from django import forms
from .models import Producto

class FormProducto(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ('categoria', 'fecha', 'titulo', 'descripcion', 'precio', 'imagen')
        widgets = {
            'categoria': forms.Select(
                attrs={
                    "class": "form-control",
                    "id": "categoria",
                }
            ),
            'fecha': forms.SelectDateWidget(
                attrs={
                    "class": "visually-hidden",
                }
            ),
            'titulo':forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "titulo",
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    "class": "form-control",
                    "id": "descripcion",
                }
            ),
            'precio': forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "id": "precio",
                }
            ),
            'imagen': forms.ClearableFileInput(),
        }


