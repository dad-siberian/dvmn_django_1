from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from places.models import Photo, Place


def show_main(request):
    places = Place.objects.all()
    serialize_places = {"type": "FeatureCollection", "features": []}
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
        serialize_places["features"].append(feature)

    return render(request, "index.html", {"places_info": serialize_places})


def show_place_detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    serialize_place = {
        "title": place.title,
        "imgs": [img.photo.url for img in Photo.objects.filter(place=place)],
        "short_description": place.short_description,
        "long_description": place.long_description,
        "coordinates": {
            "lat": place.lat,
            "lng": place.lng,
        },
    }

    return JsonResponse(
        data=serialize_place,
        json_dumps_params={"ensure_ascii": False, "indent": 4},
    )
