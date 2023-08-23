# videos/admin.py
from django.contrib import admin
from .models import Video

# Override the default admin site header and title
admin.site.site_header = "Cyber Home Admin"
admin.site.site_title = "Cyber Admin"

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'watched')
    list_filter = ('watched',)
    search_fields = ('title', 'author')
    ordering = ('-id',)

    readonly_fields = ('thumbnail_preview',)  # Add this line

    def thumbnail_preview(self, obj):
        return f'<img src="{obj.thumbnail}" width="100" height="100" alt="Thumbnail">'
    thumbnail_preview.allow_tags = True
    thumbnail_preview.short_description = 'Thumbnail'

admin.site.register(Video, VideoAdmin)
