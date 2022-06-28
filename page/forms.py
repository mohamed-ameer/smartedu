from django import forms
from page.models import Page

class NewPageForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate'}), required=True)
	video_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate'}), required=True)
	description = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate'}), required=True)
	files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

	class Meta:
		model = Page
		fields = ('title','video_url','description', 'files')