import json

from django.shortcuts import render


def show_main(request):
    files = {
        "roofs24": "static/places/roofs24.json",
        "moscow_legends": "static/places/moscow_legends.json",
    }
    places_info = {"type": "FeatureCollection", "features": []}
    for place_id, file_path in files.items():
        with open(file_path, "r") as file:
            place = json.load(file)
            feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        place["coordinates"]["lng"],
                        place["coordinates"]["lat"],
                    ],
                },
                "properties": {
                    "title": place["title"],
                    "placeId": place_id,
                    "detailsUrl": file_path,
                },
            }
            places_info["features"].append(feature)

    return render(request, "index.html", {"places_info": places_info})
