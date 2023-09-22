from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import UserSignupForm
import requests
from dotenv import load_dotenv
import os

load_dotenv()


# Create your views here.
def index(request):
    return render(request, "index.html")

def AddBookView(request):
    return render(request, "addbook.html")

def SearchResultsView(request):
    query_title = request.GET['title']
    query_author = request.GET['author']
    api_key = os.environ.get('API_KEY')

    try:
        response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={query_title}+inauthor:{query_author}&key={api_key}", params=request.GET)
        response_json = response.json()

        title = response_json['items'][0]['volumeInfo']['title']
        author = response_json['items'][0]['volumeInfo']['authors'][0]
        description = response_json['items'][0]['volumeInfo']['description']
        thumbnail = response_json['items'][0]['volumeInfo']['imageLinks']['thumbnail']
        language = response_json['items'][0]['volumeInfo']['language']
        bookInfo = {
            "title": title,
            "author": author,
            "description": description,
            "thumbnail": thumbnail,
            "language": language
        }
        print(bookInfo["title"])
        return render(request, "searchResults.html", { "searchResult": bookInfo })
    except (Exception):
        return render(request, "searchResults.html", { "searchResult": None })
    
    

class SignUpView(generic.CreateView):
    form_class = UserSignupForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"



# def login(request):
#     return render(request, 'login.html')
