from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.contrib import admin
from django.db.models import Prefetch
from django.utils.html import format_html

from .models import Photo, Place

PHOTO_MAX_HEIGHT = 200
PHOTO_MAX_WIDTH = 200


class PhotoInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Photo
    readonly_fields = ("get_preview",)

    def get_preview(self, obj):
        return format_html(
            "<img src='{}' style='max-width: {}px; max-height: {}px;'/>",
            obj.photo.url,
            PHOTO_MAX_WIDTH,
            PHOTO_MAX_HEIGHT,
        )

    def get_queryset(self, request):
        queryset = (
            super()
            .get_queryset(request)
            .prefetch_related(Prefetch("place__photos"))
        )

        return queryset


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("title",)
    inlines = [PhotoInline]
    search_fields = ("title",)


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    autocomplete_fields = ["place"]
