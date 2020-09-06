from django import forms

class RequestForm(forms.Form):
    text = forms.CharField(widget=forms.TextInput(attrs={'value': '请输入关键词','onfocus':'javascript:if(this.value==\'请输入关键词\')this.value=\'\';'}))
    # start_time = forms.DateField(widget=forms.DateInput(format='%Y%m'), input_formats=['%Y%m'])
    start_time = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    last_time = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))