from django import forms
from .models import Meeting, MeetingMinutes, Resource, Event

class MeetingForm(forms.ModelForm):
    class Meta:
        model=Meeting
        fields='__all__'

class ResourceForm(forms.ModelForm):
    class Meta:
        model=Resource
        fields='__all__'


class MeetingMinutesTestForm(forms.ModelForm):
    class Meta:
        model=MeetingMinutes
        fields='__all__'