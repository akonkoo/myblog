from django.contrib import admin
from blog.models import Entry, Tag

from django_markdown.admin import MarkdownModelAdmin

class EntryAdmin(MarkdownModelAdmin):
	list_display = ('title', 'created')

admin.site.register(Entry, EntryAdmin)
admin.site.register(Tag)