from django.contrib import admin

from .models import Category, Book


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'category', 'slug', 'price', 'created_at', 'updated_at']
    list_filter = ['category', 'created_at', 'updated_at']
    list_editable = ['price', ]
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'created_at'
    list_display_links = ('name', 'category')


admin.site.register(Book, BookAdmin)
