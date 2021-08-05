from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["description", "start_time", "end_time"]
        labels = {"description": "", "start_time": "", "end_time": ""}
