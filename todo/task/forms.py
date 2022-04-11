from dataclasses import field
from turtle import done
from django import forms

from .models import Task

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('title', 'description')