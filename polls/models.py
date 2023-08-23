import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin
# from django.contrib.auth.models import User

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    option_one = models.CharField(max_length=50)
    option_two = models.CharField(max_length=50)
    option_three = models.CharField(max_length=50)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    # author = models.ForeignKey(
    #     to=User,
    #     on_delete=models.CASCADE,
    #     editable=False
    # )

    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )

    # def get_absolute_url(self):
    #     return reverse('detail', kwargs={'cat_slug': self.slug})


    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=100)
#     votes = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.choice_text
#
