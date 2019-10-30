from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index' ),
    path('register/', views.register, name ='register'),
    path('home/', views.home, name='home' ),
    path('search/', views.search_results, name='search_results'),
    path('news/', UpdateListView.as_view(), name='news'),
    path('estate/', views.estate , name='estate'),
    path('post/new', UpdateCreateView.as_view(), name='create-post'),
    path('profile/', views.profile, name='profile'),



]