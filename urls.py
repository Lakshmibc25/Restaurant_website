from django.urls import path
from .views import home_view, menu_view, contact_view

urlpatterns = [
    path("", home_view, name="home"),
    path("menu/", menu_view, name="menu"),
    path("contact/", contact_view, name="contact"),
]
