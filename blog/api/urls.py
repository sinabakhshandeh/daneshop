from django.urls import path

from blog.api import views

urlpatterns = [
    path("", views.post_list_api),
    path("<slug:post_slug>", views.post_details_view_api),
    path("tag/<slug:category_slug>", views.post_list_api),
]
