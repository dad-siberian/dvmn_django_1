from django.db.models import Prefetch
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from places.models import Place


def show_main(request):
    places = Place.objects.all()
    features = [
        {
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
        for place in places
    ]
    context = {
        "places_info": {"type": "FeatureCollection", "features": features}
    }

    return render(request, "index.html", context)


def show_place_detail(request, place_id):
    place = get_object_or_404(
        Place.objects.prefetch_related(Prefetch("photos")), id=place_id
    )
    serialize_place = {
        "title": place.title,
        "imgs": [img.photo.url for img in place.photos.all()],
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
