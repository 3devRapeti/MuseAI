from django import forms

class KeywordForm(forms.Form):
    Keyword = forms.CharField(label="Enter Keyword", error_messages={"required":"Empty"}, max_length=100)
    Model = forms.ChoiceField(choices=[('basic', 'Normal'), ('premium', 'Upgraded')], required=True, initial='basic')