from django.contrib import admin
from book.models import *
# Register your models here.

admin.site.register(Emenitites)
admin.site.register(Movie)


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_url')