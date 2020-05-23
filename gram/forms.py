from django import forms
from .models import Gram,Reply
class ImageUpload(forms.ModelForm):

    class Meta:
        model = Gram
        fields = ["Photo","comment","author"]

class ReplyForm(forms.ModelForm):

    class Meta:
        model = Reply
        exclude = ("post","author")
        fields = ["reply",]
