from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class Topic(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'

class Discussion(models.Model):
    title = models.CharField(max_length=60)
    discussion_topic = models.ForeignKey(Topic, on_delete=CASCADE)
    discussion_picture = models.ImageField(null = True, blank=True)
    content = models.TextField(max_length=2000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_time = models.DateTimeField(auto_now=True)
    updated = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Discussion'
        verbose_name_plural = 'Discussions'

