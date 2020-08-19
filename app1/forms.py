from django import forms

from .models import Topic, Entry


class NewTopic(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['tittle']
        labels = {'tittle': ''}

class NewEntry(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
