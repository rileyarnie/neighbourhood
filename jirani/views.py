from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib import messages
from .models import Neighbourhood, Business
from django.views.generic import *
from .models import Updates, Business
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'jirani/home.html',)

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

class BizansListView(ListView):
    model = Business
    template_name = 'jirani/news.html'
    context_object_name = 'biznas'

def estate(request):
    updates = Updates.objects.all()
    biznas = Business.get_business()

    context = {"updates": updates, "biznas":biznas}

    return render(request,'jirani/estate.html', context)

class UpdateCreateView(LoginRequiredMixin, CreateView):
    model = Updates
    fields = ['title','estate', 'content']
    success_url='/estate'

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account Updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)


    context={
        'u_form': u_form,
        'p_form': p_form,

    }
    return render(request, 'users/profile.html', context)