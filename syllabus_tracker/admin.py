from django.contrib import admin

from .models import (
Subject,
Unit,
Topic,
TopicProgress,
StudyStreak,
WeeklyGoal,
StudySession,
RevisionTask,
Achievement
)

admin.site.register(Subject)
admin.site.register(Unit)
admin.site.register(Topic)
admin.site.register(TopicProgress)

admin.site.register(StudyStreak)
admin.site.register(WeeklyGoal)
admin.site.register(StudySession)

admin.site.register(RevisionTask)
admin.site.register(Achievement)
