
from django import forms

CITIES = (
  (1, 'Москва'),
  (2, 'Санкт-Петербург'),
  (3, 'Новосибирск'),
  (4, 'Екатеринбург'),
  (5, 'Владивосток'),
)


class AddressForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    address = forms.CharField(
        label='Адрес',
        widget=forms.TextInput(attrs={'placeholder': 'Адрес'})
    )
    city = forms.ChoiceField(choices=CITIES)


class FinalForm(forms.Form):
    address = forms.CharField(
        label='Адрес',
        widget=forms.TextInput(attrs={'placeholder': 'Адрес'})
    )
    city = forms.ChoiceField(choices=CITIES)
    email = forms.CharField(widget = forms.HiddenInput(), required = False)
    name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(attrs={'placeholder': 'Имя'})
    )
