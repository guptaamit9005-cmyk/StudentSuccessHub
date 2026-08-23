from django.contrib import admin

from .models import (
    LabSubject,
    LabQuestion
)


admin.site.register(
    LabSubject
)

admin.site.register(
    LabQuestion
)