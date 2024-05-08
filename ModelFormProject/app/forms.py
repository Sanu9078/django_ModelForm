from django import forms
from app.models import *
class TopicModel(forms.ModelForm):
    class Meta:
        model = Topic
        fields='__all__'

class WebsiteModel(forms.ModelForm):
    class Meta:
        model = Website
        fields = '__all__'

class AccessModel(forms.ModelForm):
    class Meta:
        model = Access
        fields = '__all__'