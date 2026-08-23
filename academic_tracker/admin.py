from django.contrib import admin

from .models import (
Subject,
Unit,
Topic,
TopicProgress
)

admin.site.register(Subject)
admin.site.register(Unit)
admin.site.register(Topic)
admin.site.register(TopicProgress)
