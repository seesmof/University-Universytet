from django.shortcuts import render
import requests

from .models import HistoryItem
from .consts import BIBLE_BOOK_NUMBER_TO_HOMENKO_BIBLE_NAME


def index(request):
    if request.method == "POST":
        text = request.POST.get("search")

        # Remember search text
        history_item = HistoryItem.objects.create(text=text)
        history_item.save()

        base_url = f"https://bolls.life/v2/find/UBIO?search={text}&limit=10"
        response = requests.get(base_url)
        data = response.json()["results"]

        # Add a readable verse reference to each verse:
        for verse in data:
            Book_number = verse["book"]
            Book_name = BIBLE_BOOK_NUMBER_TO_HOMENKO_BIBLE_NAME[Book_number]

            verse["reference"] = f"{Book_name} {verse['chapter']}:{verse['verse']}"

        context = {"verses": data, "request": text}
        return render(request, "verses.html", context)

    else:
        history = HistoryItem.objects.all()

        context = {"history": history}
        return render(request, "index.html", context)
