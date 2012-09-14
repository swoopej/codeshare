from django.contrib import admin
from cab.models import Language, Snippet

class LanguageAdmin(admin.ModelAdmin):
	prepopulated_fields = { 'slug': ['name']}

admin.site.register(Language, LanguageAdmin)

class SnippetAdmin(admin.ModelAdmin):
	prepopulated_fields = { 'slug': ['title']}

admin.site.register(Snippet, SnippetAdmin)