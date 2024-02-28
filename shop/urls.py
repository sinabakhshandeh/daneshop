from django.urls import path

from shop import views

urlpatterns = [
    path("", views.shop_product_list_view),
]
