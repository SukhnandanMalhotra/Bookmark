from django.contrib import admin

from django.contrib import admin
from .models import Bookmark, Tags


class BookmarkModelAdmin(admin.ModelAdmin):
    list_display = ['name','url','date_time_posted','is_public', 'get_tags']
    list_filter = ['tags']
    search_fields = ['user__username','name']

    def get_tags(self, bookmark):
        return ','.join([tags.name for tags in bookmark.tags.all()])


admin.site.register(Bookmark, BookmarkModelAdmin)
admin.site.register(Tags)
