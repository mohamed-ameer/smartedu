from django import forms
from assignment.models import Assignment, Submission
from django.forms.widgets import NumberInput

class NewAssignmentForm(forms.ModelForm):
    assignment_type = (
    ('Regular_File', 'Regular_File'),
    ('Programming_File', 'Programming_File'),
    )
    language_type = (
    ('None', 'None'),
    ('C', 'C'),
    ('C++', 'C++'),
    ('Java', 'Java'),
    ('Python', 'Python'),
    )
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate'}), required=True)
    assignment_type = forms.ChoiceField(required=True, choices=assignment_type)
    language_type = forms.ChoiceField(required=True, choices=language_type)
    points = forms.IntegerField(max_value=100, min_value=1)
    due = forms.DateField(widget=NumberInput(attrs={'type': 'date'})) 
    # files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': False}), required=False)
    class Meta:
        model = Assignment
        fields = ('title', 'points','assignment_type','language_type', 'due', 'file')

class NewSubmissionForm(forms.ModelForm):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': False}), required=True)
    comment = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate'}), required=False)

    class Meta:
        model = Submission
        fields = ('file','assignment_type','language_type', 'comment')