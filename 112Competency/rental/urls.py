from django.urls import path
from . import views

#add objects to map urls with actions in the view.py

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='home'),
    path('developer', views.developer, name='devName'),
    path('catalog', views.catalog, name='catalog'),
    path('details/<int:movie_id>', views.details, name='details'),
]