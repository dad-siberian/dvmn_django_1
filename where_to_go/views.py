from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from places.models import Photo, Place


def show_main(request):
    places = Place.objects.all()
    places_info = {"type": "FeatureCollection", "features": []}
    for place in places:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lng, place.lat],
            },
            "properties": {
                "title": place.title,
                "placeId": place.pk,
                "detailsUrl": reverse(
                    show_place_detail, kwargs={"place_id": place.pk}
                ),
            },
        }
        places_info["features"].append(feature)

    return render(request, "index.html", {"places_info": places_info})


def show_place_detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    place_info = {
        "title": place.title,
        "imgs": [img.photo.url for img in Photo.objects.filter(place=place)],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lat": place.lat,
            "lng": place.lng,
        },
    }

    return JsonResponse(
        data=place_info, json_dumps_params={"ensure_ascii": False, "indent": 4}
    )
