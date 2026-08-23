from django.contrib import admin

from .models import (
    Company,
    JobOpening,
    PlacementApplication,
    InterviewRound,
    Skill,
)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "company_type",
        "location",
        "website",
        "created_at",
    )

    search_fields = (
        "name",
        "location",
        "company_type",
    )

    list_filter = (
        "company_type",
    )

    ordering = (
        "name",
    )


@admin.register(JobOpening)
class JobOpeningAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "company",
        "job_type",
        "package",
        "last_date",
        "is_active",
    )

    search_fields = (
        "title",
        "company__name",
    )

    list_filter = (
        "job_type",
        "is_active",
    )

    list_editable = (
        "is_active",
    )

    ordering = (
        "-created_at",
    )


@admin.register(PlacementApplication)
class PlacementApplicationAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "job",
        "status",
        "applied_on",
    )

    search_fields = (
        "user__username",
        "job__title",
    )

    list_filter = (
        "status",
    )

    ordering = (
        "-applied_on",
    )


@admin.register(InterviewRound)
class InterviewRoundAdmin(admin.ModelAdmin):

    list_display = (
        "application",
        "round_type",
        "interview_date",
        "completed",
    )

    search_fields = (
        "application__user__username",
    )

    list_filter = (
        "round_type",
        "completed",
    )

    list_editable = (
        "completed",
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):

    list_display = (
        "name",
    )

    search_fields = (
        "name",
    )