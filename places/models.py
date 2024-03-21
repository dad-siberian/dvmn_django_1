from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    """
    Класс, представляющий место на карте с описанием и координатами

    """

    title = models.CharField(
        max_length=200, blank=True, verbose_name="Название места"
    )
    description_short = models.TextField(
        blank=True, verbose_name="Короткое описание"
    )
    description_long = HTMLField(blank=True, verbose_name="Полное описание")
    lng = models.FloatField(verbose_name="Долгота в градусах")
    lat = models.FloatField(verbose_name="Широта в градусах")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["pk"]


class Photo(models.Model):
    """
    Класс, представляющий фотографию, связанную с местом

    """

    place = models.ForeignKey(
        Place, on_delete=models.CASCADE, related_name="photos"
    )
    photo = models.ImageField(
        upload_to="places", null=True, blank=True, verbose_name="Фото"
    )
    position = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.position} {self.place.title}"

    class Meta:
        ordering = ["position"]
