from blog import views
from django.urls import path

urlpatterns = [
    path("", views.post_list, name="home"),
    path("post/<int:pk>/", views.post_detail, name="post_detail"),
]
