from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt
from .models import Image, Profile, Comment, User
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from .email import send_welcome_email

# Create your views here.


def login(request):
    '''
    This is where a user logs in after signing up to the app
    '''
    return render(request, 'registration/login.html')


def registration_form(request):
    return render(request, 'registration/registration_form.html')


@login_required(login_url='/accounts/login/')
def home(request):
    '''
    This is the current user's profile page
    '''
    images = Image.objects.all()
    date = dt.date.today()
    profiles = Profile.objects.all()
    comments = Comment.objects.all()
    users = User.objects.all()

    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.save()
            return redirect('home')

    else:
        form = CommentForm()

    return render(request, 'home.html', {'images': images, 'commentForm': form, 'date': date, 'profiles': profiles, 'comments': comments, 'users':user})


@login_required(login_url='/accounts/login/')
def profile(request, id):
    current_user = request.user
    profiles = Profile.objects.get(user=current_user)
    images = Image.objects.filter(user=current_user)

    return render(request, 'profile.html', {'profile': profiles, "images": images})


@login_required(login_url='/accounts/login/')
def user(request):
    users = User.objects.all()
    images = Image.objects.all()

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


def new_comment(request, post_id):
    post = get_object_or_404(Image, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
    return redirect('home')
