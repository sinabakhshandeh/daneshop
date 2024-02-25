from django.urls import include, path

urlpatterns = [
    path("posts/", include("blog.api.urls")),
    path("products/", include("shop.api.urls")),
]
