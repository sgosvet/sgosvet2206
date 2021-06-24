from django.forms import *
from home.models import ContactUs

# Creo un formulario con los campos del Modelo
class ContactUsForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
                
    class Meta:
        model = ContactUs
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                }
            ),
            'mensaje': Textarea(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                    'rows': 3,
                    'cols': 3
                }
            ),
        }
        exclude = ('fecha',)
        
    
    # Sobreescribimos el método save() del form para enviar los datos por ajax
    def save(self, *args, **kwargs):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
    
    # Sobreescibir el método que contiene los errores del formulario
    def clean(self):
        cleaned = super().clean() # Devuelve un diccionario {'campo':'valor', ...}
        # Podemos agregarle validaciones a los campos del formulario enviado
        # if len(cleaned['name']) <= 50:
        #     self.add_error('name', 'Le faltan carácteres')
        # print(cleaned)
        return cleaned

