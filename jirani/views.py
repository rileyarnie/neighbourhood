from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from .models import Neighbourhood, Business
from django.views.generic import ListView
from .models import Updates


# Create your views here.

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'jirani/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Account created! Log In Now!')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def search_results(request):
    if 'biz' in request.GET and request.GET['biz']:
        search_term = request.GET.get('biz')
        searched_biznas = Business.search_by_hood(search_term)
        message = f"{search_term}"
        print(message)
        print(searched_biznas)
        return render(request, 'jirani/search.html', {"message": message, "searched_biznas": searched_biznas})


    else:
        message = "You haven't searched for any Businesses"
        return render(request, 'jirani/search.html',{"message":message})


class UpdateListView(ListView):
    model = Updates
    template_name = 'jirani/news.html'
    context_object_name = 'updates'

