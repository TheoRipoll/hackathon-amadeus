from django.db.models import Q
from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy

from .forms import LoginForm, RegisterForm
from .models import Place


# A class based view that is used to login a user.
class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'


# A class based view that is used to register a user.
class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


# A class based view that is used to display a list of places.
class PlaceView(generic.ListView):
    model = Place
    template_name = "main/place_list.html"
    paginate_by = 10


# A class based view that is used to display the details of a place.
class PlaceDetailView(generic.DetailView):
    model = Place
    template_name = 'main/place_detail.html'


# A class based view that is used to search for a place.
class SearchResultsView(generic.ListView):
    model = Place
    template_name = "search_results.html"

    # A function that is used to filter the search results.
    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Place.objects.filter(
            Q(name__icontains=query)
        )
        return object_list
