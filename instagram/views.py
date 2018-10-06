from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from .models import Image
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from .email import send_welcome_email

# Create your views here.
def registration_form(request):
    '''
    This is the page where a user signs up to the app
    '''
    return render(request,'registration/registration_form.html')

def login(request):
    '''
    This is where a user logs in after signing up to the app
    '''
    return render(request,'registration/login.html')

def profile(request):
    '''
    This is a user's profile page
    '''
    return render(request,'profile.html')    

@login_required(login_url='/accounts/register/')
def home(request):
    '''
    This is the current user's profile page
    '''
    images = Image.objects.all()
    date = dt.date.today()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        HttpResponseRedirect('home')

    else:
        form = CommentForm()

    return render(request,'home.html',{'images':images, 'commentForm':form})

@login_required(login_url='/accounts/login/')
def profile(request):
    profiles =  Profile.objects.all()

    return render(request, 'home.html')

@login_required(login_url='/accounts/login/')
def like(request, image_id):
	post = get_object_or_404(Image, pk=image_id)
	request.user.profile.like(post)

	return redirect('welcome')    

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_image_name(search_term)

        message = f"{search_term}"
        return render(request, 'search.html', {"message":message, "images": searched_images})

    else:
        message = "You haven't made any searches"
        return render(request, 'search.html', {"message":message})    
