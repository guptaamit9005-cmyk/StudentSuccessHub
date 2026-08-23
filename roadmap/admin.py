from django.contrib import admin

from .models import (
    RoadmapCategory,
    Roadmap,
    RoadmapStep
)


@admin.register(RoadmapCategory)
class RoadmapCategoryAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'icon',
        'color',
        'created_at'
    )

    search_fields = (
        'name',
    )


@admin.register(Roadmap)
class RoadmapAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'creator',
        'category',
        'difficulty',
        'progress',
        'featured'
    )

    list_filter = (
        'difficulty',
        'featured',
        'visibility'
    )

    search_fields = (
        'title',
        'description'
    )


@admin.register(RoadmapStep)
class RoadmapStepAdmin(admin.ModelAdmin):

    list_display = (
        'step_number',
        'title',
        'roadmap',
        'completed'
    )

    list_filter = (
        'completed',
    )

    search_fields = (
        'title',
    )