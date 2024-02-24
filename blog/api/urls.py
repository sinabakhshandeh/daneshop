from django.urls import path

from blog.api import views

urlpatterns = [
    path("", views.post_list_api),
]
