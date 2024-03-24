from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from .models import Photo, Place

admin.site.register(Photo)

PHOTO_MAX_HEIGHT = 200


class PhotoInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Photo
    readonly_fields = ("get_preview",)

    def get_preview(self, obj):
        return format_html(
            "<img src='{}' style='max-height: {}px;'/>",
            obj.photo.url,
            PHOTO_MAX_HEIGHT,
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("title",)
    inlines = [PhotoInline]
