from django.shortcuts import render
import requests

from .consts import BIBLE_BOOK_NUMBER_TO_HOMENKO_BIBLE_NAME


def index(request):
    if request.method == "POST":
        text = request.POST.get("search")

        base_url = f"https://bolls.life/v2/find/UBIO?search={text}&limit=10"
        response = requests.get(base_url)
        data = response.json()["results"]

        # Add a readable verse reference to each verse:
        for verse in data:
            Book_number = verse["book"]
            Book_name = BIBLE_BOOK_NUMBER_TO_HOMENKO_BIBLE_NAME[Book_number]

            verse["reference"] = f"{Book_name} {verse['chapter']}:{verse['verse']}"
            print(verse["reference"])

        context = {"verses": data, "request": text}
        return render(request, "verses.html", context)

    else:
        return render(request, "index.html", {})
