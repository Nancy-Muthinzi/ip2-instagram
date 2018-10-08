from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt
from .models import Image, Profile
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from .email import send_welcome_email

# Create your views here.
def login(request):
    '''
    This is where a user logs in after signing up to the app
    '''
    return render(request, 'registration/login.html')


@login_required(login_url='/accounts/login/')
def profile(request):
    '''
    This is a user's profile page
    '''
    return render(request, 'home.html')


@login_required(login_url='/accounts/login/')
def home(request):
    '''
    This is the current user's profile page
    '''
    images = Image.objects.all()
    date = dt.date.today()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        return redirect('home')

    else:
        form = CommentForm()

    return render(request, 'home.html', {'images': images, 'commentForm': form})


@login_required(login_url='/accounts/login/')
def profile(request):
    profiles = Profile.objects.all()

    return render(request, 'home.html')


@login_required(login_url='/accounts/login/')
def search_results(request):

    if 'user' in request.GET and request.GET["user"]:
        search_term = request.GET.get("user")
        searched_users = User.search_by_user_name(search_term)

        message = f"{search_term}"
        return render(request, 'search.html', {"message": message, "users": searched_users})

    else:
        message = "You haven't made any searches"
        return render(request, 'search.html', {"message": message})
