from django.urls import path

from shop import views

app_name = "shop"

urlpatterns = [
    path("", views.shop_product_list_view, name="home"),
]
