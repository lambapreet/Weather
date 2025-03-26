from django.forms import ModelForm, TextInput
from .models import City  # Updated import to match corrected model name

class CityForm(ModelForm):
    class Meta:
        model = City  # Changed from 'city' to 'City'
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class': 'input', 'placeholder': 'City Name'})  # Fixed 'placeholder' typo
        }


'''
from django.forms import ModelForm, TextInput
from .models import City  # Changed to match the improved model name (PascalCase)

class CityForm(ModelForm):
    """
    Form for creating/editing City instances.
    
    Attributes:
        Meta.model: Specifies the City model
        Meta.fields: Includes all fields from the model
        Meta.widgets: Customizes the form field widgets
    """
    class Meta:
        model = City  # Matches the model name
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',  # More standard Bootstrap class
                'placeholder': 'Enter city name',  # Corrected spelling
                'autocomplete': 'off'  # Useful for location fields
            })
        }
        labels = {
            'name': 'City'  # Custom label for the field
        }
        help_texts = {
            'name': 'Enter the name of the city'  # Help text
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Additional initialization if needed
        self.fields['name'].widget.attrs.update({
            'aria-label': 'City name input'  # Accessibility improvement
        })
'''