from django import forms
from .models import Question, Answer

class QuestionCreateForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['questioner_name', 'questioner_email', 'photo', 'quest']

class AnswerCreateForm(forms.ModelForm):
    ans = forms.CharField( widget=forms.Textarea(attrs={'class': 'form-control', 'cols': 80, 'rows': 5}) )
    class Meta:
        model = Answer
        fields = ['ans',]