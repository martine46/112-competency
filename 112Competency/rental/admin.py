from django.contrib import admin
from .models import Genre, Movie

# Create Admin templates 
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class MovieAdmin(admin.ModelAdmin):
    list_dislay = ('id', 'title', 'release_year', 'price', 'in_stock')
    # exclude = ('in_stock', 'price')
    fields = ('id', 'title', 'genre', 'in_4k')

# Register models here.
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)

