from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Book, BookInstance, Author, Genre, Language


admin.site.register(Genre)
admin.site.register(Language)

@register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "date_of_birth", "date_of_death")

@register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "display_genre")

@register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ("book", "status", "due_back")