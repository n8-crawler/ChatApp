from django.forms import ModelForm
from .models import Room
from django.contrib.auth.models import User

class Roomform(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

class Userform(ModelForm):
    class Meta:
        model = User
        fields = ['username','email']