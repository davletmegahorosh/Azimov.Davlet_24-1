from django import forms

class ProductCreateForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea())
    rate = forms.FloatField()

class CommentCreateForm(forms.Form):
    text = forms.CharField()
