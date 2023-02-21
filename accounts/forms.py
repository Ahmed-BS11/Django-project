from django.forms import ModelForm
from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        #najmou njibou fields mou3aynin n3aytelhom fi list 
        #fiels=['aaa','bbb']