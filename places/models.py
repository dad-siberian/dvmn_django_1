from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description_short = models.TextField()
    description_long = HTMLField()
    lng = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["pk"]


class Photo(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    photo = models.ImageField(
        upload_to="places", null=True, blank=True, verbose_name="Фото"
    )
    position = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.position} {self.place.title}"

    class Meta:
        ordering = ["position"]
