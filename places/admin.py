from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from .models import Photo, Place

admin.site.register(Photo)


class PhotoInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Photo
    readonly_fields = ("get_preview",)

    def get_preview(self, obj):
        return format_html("<img src='{}' height='200px'/>", obj.photo.url)


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("title",)
    inlines = [PhotoInline]
