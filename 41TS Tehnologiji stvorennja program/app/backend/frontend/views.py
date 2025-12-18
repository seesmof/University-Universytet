from django.shortcuts import render
import requests

"""
def index(request):
    base_url = f"https://bolls.life/v2/find/UBIO?search=Гріх"
    try:
        response = requests.get(base_url)
        data = response.json()
        print(data)

        context = {"verses": data}
        return render(request, "index.html", context)

    except requests.exceptions.RequestException as e:
        error_message = f"Failed fetching from Bolls.Life, {e}"
        context = {"error": error_message}
        return render(request, "error.hmtl", context)
"""


def index(request):
    if request.method == "POST":
        text = request.POST.get("search")

        base_url = f"https://bolls.life/v2/find/UBIO?search={text}&limit=10"
        response = requests.get(base_url)
        data = response.json()["results"]
        print(data)

        context = {"verses": data, "request": text}
        return render(request, "verses.html", context)

    else:
        return render(request, "index.html", {})
