from django.contrib import admin

# Register your models here.
from .models import Douban


class DoubanAdmin(admin.ModelAdmin):
    list_display = ('author', 'comments', 'star')
    search_fields = ('comments',)

admin.site.register(Douban , DoubanAdmin,)