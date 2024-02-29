from django.urls import path

from cart import views

app_name = "cart"

urlpatterns = [
    path("<uuid:cart_uuid>/", views.cart_details, name="cart_details"),
    path("add/item/", views.add_item, name="add_item"),
    path("pay/", views.pay, name="pay"),
]
