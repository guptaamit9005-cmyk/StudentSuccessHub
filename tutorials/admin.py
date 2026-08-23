from django.contrib import admin
from .models import Category, Tutorial, Bookmark, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "category",
        "level",
        "featured",
        "views",
        "created_at",
    )

    list_filter = (
        "category",
        "level",
        "featured",
    )

    search_fields = (
        "title",
        "content",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "tutorial",
        "created_at",
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "tutorial",
        "created_at",
    )

    search_fields = (
        "comment",
    )