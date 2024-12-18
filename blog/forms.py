from django import forms



class OrderForm(forms.Form):
    first_name = forms.CharField(
        max_length=30,
        required=True,
        label='Имя',
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        label="Фамилия",
    )
    surname = forms.CharField(
        max_length=30,
        required=False,
        label="Отчество",
    )
    phone = forms.CharField(
        max_length=20,
        required=True,
        label="Номер телефона",
    )
    email = forms.EmailField(
        required=False,
        label="E-mail",
    )
    city = forms.CharField(
        max_length=40,
        required=True,
        label="Город",
    )
    address = forms.CharField(
        max_length=255,
        required=True,
        label="Адрес",
    )
    index = forms.IntegerField(
        required=True,
        label='Индекс'
    )

