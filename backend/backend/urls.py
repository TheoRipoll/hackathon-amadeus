from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import include, path
from django.views.generic.base import TemplateView

from main.views import LoginView, RegisterView, PlaceDetailView, PlaceView, SearchResultsView, FavouriteView, add_place, \
    remove_place

# A list of url patterns.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='main/index.html'), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('places/', PlaceView.as_view(), name='place_list'),
    path('places/<slug:slug>', PlaceDetailView.as_view(), name='place_detail'),
    path('search/', SearchResultsView.as_view(), name="search_results"),
    path('places/<int:pk>/add', add_place, name='add_place'),
    path('places/<int:pk>/remove', remove_place, name='remove_place'),
    path('favourites/', FavouriteView.as_view(), name='favourite_list'),
]
