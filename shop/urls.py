from django.urls import path

from shop import views

app_name = "shop"

urlpatterns = [
    path("", views.shop_product_list_view, name="home"),
    path(
        "<slug:product_slug>",
        views.shop_product_details_view,
        name="product_details",
    ),
]
