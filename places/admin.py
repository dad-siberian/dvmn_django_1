from django.contrib import admin
from .models import Place, Photo

admin.site.register(Photo)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ("title",)
