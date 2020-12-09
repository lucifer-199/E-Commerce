
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Shop Home"),
    path("about/", views.about, name="About us"),
    path("contact/", views.contact, name="Contact us"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.productView, name="productview"),
    path("checkout/", views.checkout, name="Checkout")
]
