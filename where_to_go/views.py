from django.shortcuts import render

from places.models import Place


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
                # "detailsUrl": file_path,
            },
        }
        places_info["features"].append(feature)

    return render(request, "index.html", {"places_info": places_info})
