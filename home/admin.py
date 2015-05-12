# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Tag, Video, Comment

class TagAdmin(admin.ModelAdmin):
	list_display = ('name', 'description',)
	search_fields = ('name', 'description',)

class VideoAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'user', 'state', 'datetime',)
	search_fields = ('name', 'description',)
	list_filter = ('state', 'tags', 'datetime',)
	filter_horizontal = ('tags',)
	def has_add_permission(self, request):
		return False

class CommentAdmin(admin.ModelAdmin):
	list_display = ('text', 'user', 'video', 'datetime',)
	search_fields = ('text',)
	list_filter = ('datetime',)

admin.site.register(Tag, TagAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Comment, CommentAdmin)
