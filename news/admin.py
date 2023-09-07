from django.contrib import admin
from .models import Post, Author, Category, Comment


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Comment)


def nullfy_quantity(modeladmin, request, queryset): # все аргументы уже должны быть вам знакомы, самые нужные из них это request — объект хранящий информацию о запросе и queryset — грубо говоря набор объектов, которых мы выделили галочками.
    queryset.update(quantity=0)
nullfy_quantity.short_description = 'Обнулить товары'

class PostAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = [field.name for field in Post._meta.get_fields()]
    list_display = ['title', 'author', 'dateCreation']

    list_filter = ['title', 'author', 'dateCreation', 'postCategory']
    search_fields = ['title', 'author', 'dateCreation', 'postCategory']
    actions = [nullfy_quantity]


admin.site.register(Post, PostAdmin)