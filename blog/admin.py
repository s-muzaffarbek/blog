from django.contrib import admin
from .models import Category, Comment, Tag, Blog

admin.site.register([Category, Comment])

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

class TagInline(admin.TabularInline):
    model = Blog.tags.through
    extra = 0

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('user','title', 'created','views')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [TagInline]



