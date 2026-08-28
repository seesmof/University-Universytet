from django.shortcuts import render


# Create your views here.
def measurements_list(req):
    context = {
        "measurements": [
            {"name": "Oleh"},
            {"name": "Mykyta"},
        ]
    }
    return render(req, "measurements_list.html", context)
