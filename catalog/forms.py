from django import forms
from .models import Product, Version


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'image']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        prohibited_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]
        if any(word in name.lower() for word in prohibited_words):
            raise forms.ValidationError("Недопустимый формат ввода данных.")
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        prohibited_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]
        if any(word in description.lower() for word in prohibited_words):
            raise forms.ValidationError("Недопустимый формат ввода данных.")
        return description


class ProductVersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ['product', 'version_number', 'version_name', 'is_current']
        widgets = {
            'is_current': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }