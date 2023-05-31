from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description_short = models.TextField()
    description_long = models.TextField()
    lng = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return self.title


class Photo(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    photo = models.ImageField(
        upload_to="places", null=True, blank=True, verbose_name="Фото"
    )
    position = models.IntegerField()

    def __str__(self):
        return f"{self.position} {self.place.title}"
