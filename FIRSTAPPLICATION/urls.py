from django.urls import path
from FIRSTAPPLICATION import views

urlpatterns = [
    path('home',views.home),
    path('about',views.about),
    path('contact',views.contact),
    path('app',views.app),
    path('style',views.style),
]