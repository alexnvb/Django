
from django.forms import ModelForm

from .models import Bb

class BbForm(ModelForm):
    class Meta:
        model = Bb
        fields = Bbfields = ('title', 'content', 'price', 'rubric')