from django.db import models

import datetime

from django.utils import timezone
class Article(models.Model):
	article_title = models.CharField('name of Article', max_length = 50)
	article_text = models.TextField('text of Article')
	pub_date = models.DateTimeField('date of publication')

	def __str__(self):
		return self.article_title
	
	class Meta:
		verbose_name = "Thread"
		verbose_name_plural = "Threads"

	def was_published_recent(self):
		return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7)) 

class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete = models.CASCADE)
	author_name = models.CharField('author name', max_length = 70)
	comment_text = models.CharField('text of comment', max_length = 200)

	def __str__(self):
		return self.author_name

	class Meta:
		verbose_name = "Commentario"
		verbose_name_plural = "Commentarios"