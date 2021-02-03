from django import forms

myChoices = (("1","Category"),("2","Difficulty"),("3","Alphabetically"))
class OrderForm(forms.Form):
    # order_field = forms.ChoiceField(choices = myChoices)
    name = forms.CharField(label='Your choice')
