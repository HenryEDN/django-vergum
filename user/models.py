from discuss.models import Discussion
from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE, null = True)
    nickname = models.CharField(max_length=50, default="User")
    about_user = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(null = True, blank=True)

    def __str__(self):
        return self.nickname

    #Signals

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=CASCADE)
    discuss = models.ForeignKey(Discussion, on_delete=CASCADE)
    text = models.TextField(max_length=500)
    creation_time = models.DateField(auto_now=True)

    def __str__(self):
        return f'({self.discuss}) Comment {self.id} by {self.author}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

