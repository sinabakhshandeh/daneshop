from django.urls import path

from blog import views

app_name = "blog"

urlpatterns = [
    path("", views.post_list_view, name="post_list"),
    path("<slug:post_slug>", views.post_details_view, name="post_details"),
]
