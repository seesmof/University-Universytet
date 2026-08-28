from django.shortcuts import render


# Create your views here.
def index(request):
    context: dict = {"title": "Church", "heading": "Welcome to our holy church."}
    return render(request, "index.html", context)
