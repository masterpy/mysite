from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
# 投票应用

class Question(models.Model):
    question_text = models.CharField(max_length=200)#问题
    pub_date = models.DateTimeField('date published')#发布时间，(指定名字)
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def __str__(self):              # __unicode__ on Python 2
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'



class Choice(models.Model):
    question = models.ForeignKey(Question)#选项关联的问题ForeignKey
    choice_text = models.CharField(max_length=200)#选项说明
    votes = models.IntegerField(default=0)#投票数
    def __str__(self):              # __unicode__ on Python 2
        return self.choice_text


