from django.contrib import admin

from blog.models import Category, Comment, CommentReply, Post


class PostInline(admin.StackedInline):
    model = Post
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = [PostInline]
    list_display = ("name", "slug", "parent")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ("parent",)


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "published_at", "author", "category")
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "published_at"
    list_filter = ("published_at", "author", "category")


class CommentReplyInline(admin.TabularInline):
    model = CommentReply
    extra = 0  # Controls the number of empty forms to display


class CommentAdmin(admin.ModelAdmin):
    inlines = [CommentReplyInline]
    list_display = ("post", "text", "timestamp", "author", "approved")
    list_filter = ("approved",)
    search_fields = ("post__title", "text", "author__username")
    date_hierarchy = "timestamp"


class CommentReplyAdmin(admin.ModelAdmin):
    list_display = ("text", "timestamp", "author", "approved")
    search_fields = ("text",)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(CommentReply, CommentReplyAdmin)
