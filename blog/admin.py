from django.contrib import admin
from blog.models import Post, Tag


# customize how data is displayed in the admin panel
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_on", "last_modified", "status")
    list_filter = ["status"]
    search_fields = ["title", "content"]


class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
