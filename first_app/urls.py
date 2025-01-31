from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('list/',views.list_view, name='list'),
    path('listing/<str:id>/',views.listing_view, name='listing'),
    path('listing/<str:id>/edit/', views.edit_view, name='edit'),

]
