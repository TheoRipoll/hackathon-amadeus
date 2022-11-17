from django.db.models import Q
from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy

from .forms import LoginForm, RegisterForm
from .models import Place


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class PlaceView(generic.ListView):
    model = Place
    template_name = "main/place_list.html"
    paginate_by = 10


class PlaceDetailView(generic.DetailView):
    model = Place
    template_name = 'main/place_detail.html'


class SearchResultsView(generic.ListView):
    model = Place
    template_name = "search_results.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Place.objects.filter(
            Q(name__icontains=query)
        )
        return object_list
