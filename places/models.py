from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    """
    Класс, представляющий место на карте с описанием и координатами

    """

    title = models.CharField(max_length=200, verbose_name="Название места")
    short_description = models.TextField(verbose_name="Короткое описание")
    long_description = HTMLField(blank=True, verbose_name="Полное описание")
    lng = models.FloatField(verbose_name="Долгота в градусах")
    lat = models.FloatField(verbose_name="Широта в градусах")

    class Meta:
        ordering = ["pk"]

    def __str__(self):
        return self.title


class Photo(models.Model):
    """
    Класс, представляющий фотографию, связанную с местом

    """

    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name="photos",
        verbose_name="Место",
    )
    photo = models.ImageField(upload_to="places", verbose_name="Фото")
    position = models.IntegerField(
        default=0, blank=True, verbose_name="Позиция"
    )

    class Meta:
        ordering = ["position"]

    def __str__(self):
        return f"{self.position} {self.place.title}"
