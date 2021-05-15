from django.contrib import admin
from .models import Comment, Profile

admin.site.register(Comment)
admin.site.register(Profile)