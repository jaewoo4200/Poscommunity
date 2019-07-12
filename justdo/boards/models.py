from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator
from django.utils.html import mark_safe
from markdown import markdown
import math
#앱 모델(앱을 구성하는 요소들)
# Create your models here.

class Board(models.Model): #대분류:주제들 목록
	name = models.CharField(max_length=30, unique=True)
	#대주제 이름 제한:30글자
	description = models.CharField(max_length=100)
	#대주제 내용 소개- 100글자 제한

	def __str__(self):
		return self.name #대주제 이름 값 반환(쿼리셋 보기 좋게)

	def get_posts_count(self):
		return Post.objects.filter(topic__board=self).count()

	def get_last_post(self):
		return Post.objects.filter(topic__board=self).order_by('-created_at').first()

class Topic(models.Model): #소수제: 대주제 내 게시글
	subject = models.CharField(max_length=255)
	#소주제 255글자 제한 
	last_updated = models.DateTimeField(auto_now_add=True)
	#마지막 업데이트 시각
	board = models.ForeignKey(Board, related_name='topics', on_delete=models.CASCADE)
	starter = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)
	#MANY-TO-ONE 관계형 글 여러개-> 하나의 주제
	views = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.subject

	def get_page_count(self):
		count = self.posts.count()
		pages = count / 20
		return math.ceil(pages)

	def has_many_pages(self, count=None):
		if count is None:
			count = self.get_page_count()
		return count > 6

	def get_page_range(self):
		count = self.get_page_count()
		if self.has_many_pages(count):
			return range(1, 5)
		return range(1, count + 1)

	def get_last_ten_posts(self):
		return self.posts.order_by('-created_at')[:10]

class Post(models.Model): #게시글 내 포스트
	message = models.TextField(max_length=4000)
	#텍스트 입력 4000글자 제한
	topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(null=True)
	created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
	updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)

	def __str__(self):
		truncated_message = Truncator(self.message)
		return truncated_message.chars(30)

	def get_message_as_markdown(self):
		return mark_safe(markdown(self.message, safe_mode='escape'))