import json

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Photo, Place


def save_to_database(json_url):
    response = requests.get(json_url)
    response.raise_for_status()
    payload = response.json()
    place = Place(
        title=payload["title"],
        short_description=payload["description_short"],
        long_description=payload["description_long"],
        lng=payload["coordinates"]["lng"],
        lat=payload["coordinates"]["lat"],
    )
    place.save()

    for number, img_url in enumerate(payload["imgs"], 1):
        response = requests.get(img_url)
        response.raise_for_status()
        photo = Photo(place=place)
        photo.photo.save(
            f"photo_{number}.jpeg", ContentFile(response.content), save=True
        )


class Command(BaseCommand):

    help = "Добавляет локацию из JSON-файла в базу данных"

    def add_arguments(self, parser):
        parser.add_argument(
            "url", type=str, help="URL JSON-файла с информацией о локации"
        )

    def handle(self, *args, **options):
        try:
            save_to_database(options["url"])
            self.stdout.write(self.style.SUCCESS("Локация успешно добавлена"))
        except (
            json.decoder.JSONDecodeError,
            requests.exceptions.RequestException,
        ) as e:
            self.stderr.write(f"Ошибка: {e}")
