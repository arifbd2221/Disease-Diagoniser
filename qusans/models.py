from django.db import models
from clientsite.models import User
from django.utils import timezone

class Question(models.Model):
    questioner_name = models.CharField(max_length=150, blank=True, null=True)
    questioner_email = models.EmailField(blank=True, null=True)
    photo = models.ImageField(upload_to='question/facts/images/', blank=True, null=True)
    quest = models.CharField(max_length=500, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.quest

class Answer(models.Model):
    doctor = models.ManyToManyField(User, related_name='whoanswered')
    quest = models.ManyToManyField(Question, related_name='question')
    ans = models.CharField(max_length=500, blank=True, null=True)
    appreciation = models.ManyToManyField(User, related_name='accepted', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ans