from django import forms
from assignment.models import Assignment, Submission


class NewAssignmentForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate'}), required=True)
	points = forms.IntegerField(max_value=100, min_value=1)
	due = forms.DateField(widget=forms.TextInput(attrs={'class': 'datepicker'}), required=True) 
	files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

	class Meta:
		model = Assignment
		fields = ('title', 'points', 'due', 'files')

class NewSubmissionForm(forms.ModelForm):
	file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': False}), required=True)
	comment = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate'}), required=False)

	class Meta:
		model = Submission
		fields = ('file', 'comment')