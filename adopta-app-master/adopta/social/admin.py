from django.contrib import admin
from .models import Profile, Post, Relationship, Inbox

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Relationship)
admin.site.register(Inbox)