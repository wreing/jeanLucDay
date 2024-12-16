from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:dt>/", views.jeanLucDay, name= "jeanLucDay"),
    path("birthday/<str:dt>/", views.reverseJeanLucDay, name="reverseJeanLucDay"),

]