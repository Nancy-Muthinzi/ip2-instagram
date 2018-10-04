from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Image
from django.contrib.auth.decorators import login_required
from .forms import CommentForm

# Create your views here.
def signup(request):
    '''
    This is the page where a user signs up to the app
    '''
    return render(request,'registration/signup.html')

def login(request):
    '''
    This is where a user logs in after signing up to the app
    '''
    return render(request,'registration/login.html')

@login_required(login_url='/accounts/register/')
def home(request):
    '''
    This is the current user's profile page
    '''
    images = Image.objects.all()
    form = CommentForm(request.POST)
    if form.is_valid():
        print('valid')
    else:
        form = CommentForm()

    return render(request,'home.html',{'images':images, 'commentForm':form})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)

        message = f"{search_term}"
        return render(request, 'search.html', {"message":message, "images": searched_images})

    else:
        message = "You haven't made any searches"
        return render(request, 'search.html', {"message":message})    

