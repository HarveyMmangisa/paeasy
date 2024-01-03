
from django.shortcuts import render, redirect

from listing.models import Category, Listing
from .forms import SignupForm

def index(request):
    listings = Listing.objects.filter(is_sold=False) [0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories': categories,
        'listings': listings,
    })


def contact(request):
    return render(request, 'core/contact.html')

def Signup(request):
    if request.method =='POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
         form = SignupForm()

   

    return render (request, 'core/signup.html',{
        'form': form
    })
  