from django.shortcuts import render


# Create your views here.
def measurements_list(req):
    context = {
        "measurements": [
            {"value": "Oleh", "description": "Hi this is Bible"},
            {"value": "Mykyta", "description": "This is Bible too"},
        ]
    }
    return render(req, "measurements/list.html", context)
