from django.contrib import admin
from memos.models import Memo

class MemoAdmin(admin.ModelAdmin):
	list_display = ['title', 'text']
	list_filter = ['title']

admin.site.register(Memo, MemoAdmin)
# Register your models here.
