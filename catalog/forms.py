from django import forms
from .models import Product, Version


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'image']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Получаем пользователя из аргументов
        super(ProductForm, self).__init__(*args, **kwargs)

        if user:
            product = self.instance  # Получаем экземпляр продукта

            # Если пользователь не является владельцем продукта
            if product.owner != user:
                # Запретить редактирование имени и цены, если пользователь не имеет прав редактировать любые продукты
                if not user.has_perm('catalog.can_edit_any_product'):
                    self.fields['name'].disabled = True
                    self.fields['price'].disabled = True

            # Если пользователь имеет право на изменение категории и описания продукта
            if not user.has_perm('catalog.can_edit_description'):
                self.fields['description'].disabled = True

            if not user.has_perm('catalog.can_edit_category'):
                self.fields['category'].disabled = True

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