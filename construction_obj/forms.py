from django.contrib.auth.forms import forms


class DiscountForms(forms.Form):
    """Форма для ввода скидки."""
    discount = forms.DecimalField(
        label='Скидка',
        min_value=0,
        max_value=100,
        decimal_places=2,
        help_text='Введите размер скидки, % (от 0 до 100):'
    )
