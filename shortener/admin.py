from django.contrib import admin
from .models import URL

@admin.register(URL)
class URLAdmin(admin.ModelAdmin):
    list_display = ('short_code', 'original_url', 'user', 'clicks', 'created_at', 'expires_at')
    search_fields = ('short_code', 'original_url', 'user__username')
    list_filter = ('created_at', 'expires_at')
