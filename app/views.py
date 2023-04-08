from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import UserSignupForm


# Create your views here.
def index(request):
    return render(request, "index.html")


class SignUpView(generic.CreateView):
    form_class = UserSignupForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


# def login(request):
#     return render(request, 'login.html')
