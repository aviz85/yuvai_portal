from django.contrib import admin
from .models import AITool, Creation, Comment

@admin.register(AITool)
class AIToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'website')
    search_fields = ('name', 'description')

@admin.register(Creation)
class CreationAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'creation_type', 'created_at', 'updated_at')
    list_filter = ('creation_type', 'created_at', 'updated_at')
    search_fields = ('title', 'description', 'creator__username')
    filter_horizontal = ('tools_used',)
    readonly_fields = ('created_at', 'updated_at')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('creator').prefetch_related('tools_used')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('creation', 'author', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('content', 'author__username', 'creation__title')
    readonly_fields = ('created_at', 'updated_at')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('author', 'creation')