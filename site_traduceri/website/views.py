from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "website/index.html", {})


def servicii(request):
    return render(request, "website/servicii.html", {})


def costuri(request):
    return render(request, "website/costuri.html", {})


def contact(request):
    return render(request, "website/contact.html", {})
