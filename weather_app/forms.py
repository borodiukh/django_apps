from django.forms import Form, CharField


class CityForm(Form):
    city = CharField(label="City", max_length=100)