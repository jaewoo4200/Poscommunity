from django import forms
from .models import Topic, Post

class NewTopicForm(forms.ModelForm):
	message = forms.CharField(
		widget=forms.Textarea(
			attrs={'rows': 5, 'placeholder': '내용을 작성해주세요!'}
		),
		max_length=4000,
		help_text='4000글자 제한'
	)
	class Meta:
		model = Topic
		fields = ['subject', 'message']


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['message', ]