from django import forms
from .models import Event, Blog


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["description", "start_time", "end_time"]
        labels = {"description": "", "start_time": "", "end_time": ""}


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["topic", "content"]
        labels = {"topic": "", "content": ""}
