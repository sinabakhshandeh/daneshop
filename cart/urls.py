from django.urls import path

from cart import views

app_name = "cart"

urlpatterns = [
    path("<uuid:cart_uuid>", views.cart_details, name="cart_details"),
]
