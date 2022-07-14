from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("servicii", views.servicii, name="servicii"),
    path("costuri", views.costuri, name="costuri"),
    path("contact", views.contact, name="contact"),
]
