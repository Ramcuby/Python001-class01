
from django import forms

from .models import Douban

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)

class DoubanForm(forms.ModelForm):
    def clean_star(self):
        cleaned_data = self.cleaned_data['star']
        if not cleaned_data:
            raise forms.ValidationError('必须是数字！')
        return int(cleaned_data)

    class Meta:
        model = Douban
        fields = (
            'author', 'star', 'comments',
        )
