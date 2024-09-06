from django.contrib import admin

from blog.models import Comment, Post, Tag


# customize how data is displayed in the admin panel
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_on", "last_modified", "status")
    list_filter = ["status"]
    search_fields = ["title", "content"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_on", "validated", "content")
    list_filter = ("validated", "created_on")
    search_fields = ("name", "email", "content")
    actions = ["validate_comment"]

    def validate_comment(self, request, queryset):
        queryset.update(validated=True)


# admin.site.register(Post, PostAdmin)
# admin.site.register(Tag, TagAdmin)
