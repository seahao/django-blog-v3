from django.contrib import admin
from blogging.models import Post, Category


class InlineModelAdmin(admin.TabularInline):
    model = Category.posts.through
    extra = 2


class PostAdmin(admin.ModelAdmin):
    inlines = [
        InlineModelAdmin,
    ]


class CategoryAdmin(admin.ModelAdmin):
    exclude = ("posts",)


try:
    admin.site.unregister(Category)
except admin.sites.NotRegistered:
    pass

admin.site.register(Post, PostAdmin)
# admin.site.register(Category)
# admin.site.unregister(Category)
admin.site.register(Category, CategoryAdmin)
