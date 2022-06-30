from django import forms
from quiz.models import Quizzes, Question, Answer
from django.forms.widgets import NumberInput
class NewQuizForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate'}), required=True)
	due = forms.DateField(widget=NumberInput(attrs={'type': 'date'}), required=True)
	time_limit_mins = forms.IntegerField(max_value=360, min_value=10)

	class Meta:
		model = Quizzes
		fields = ('title', 'due', 'time_limit_mins')


class NewQuestionForm(forms.ModelForm):
	question_text = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate'}), required=True)
	points = forms.IntegerField(max_value=100, min_value=1)

	class Meta:
		model = Question
		fields = ('question_text', 'points')