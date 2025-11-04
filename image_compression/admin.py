from django.contrib import admin
from django.utils.html import format_html
from .models import CompressImage
import os



class CompressImageAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        try:
            if obj.compressed_image and os.path.exists(obj.compressed_image.path):
                return format_html(f'<img src="{obj.compressed_image.url}" width="40" height="40" />')
            else:
                return format_html('<span style="color:red;">No image</span>')
        except Exception:
            return format_html('<span style="color:red;">No image</span>')

    def original_image_size(self, obj):
        try:
            if obj.original_image and os.path.exists(obj.original_image.path):
                size_mb = obj.original_image.size / (1024 * 1024)
                return format_html(f'<span>{size_mb:.2f} MB</span>')
            else:
                return format_html('<span style="color:red;">Missing file</span>')
        except Exception:
            return format_html('<span style="color:red;">Missing file</span>')

    def compressed_image_size(self, obj):
        try:
            if obj.compressed_image and os.path.exists(obj.compressed_image.path):
                size_in_mb = obj.compressed_image.size / (1024 * 1024)
                if size_in_mb > 1:
                    return format_html(f'<span>{size_in_mb:.2f} MB</span>')
                else:
                    size_in_kb = obj.compressed_image.size / 1024
                    return format_html(f'<span>{size_in_kb:.2f} KB</span>')
            else:
                return format_html('<span style="color:red;">Missing file</span>')
        except Exception:
            return format_html('<span style="color:red;">Missing file</span>')

    list_display = ('user', 'thumbnail', 'original_image_size', 'compressed_image_size', 'compressed_at')



admin.site.register(CompressImage, CompressImageAdmin)