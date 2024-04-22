from django.contrib import admin

from vlog.models import Vlog


@admin.register(Vlog)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'text']
    search_fields = ['name', 'text']