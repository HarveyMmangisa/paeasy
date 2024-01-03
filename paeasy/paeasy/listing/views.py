from django.contrib.auth.decorators import login_required
from django.shortcuts import render,  get_object_or_404, redirect
from .forms import NewListingForm
from .models import Listing

def detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    related_listings = Listing.objects.filter(category= listing.category, is_sold=False ).exclude(pk=pk)[0:3]
      

    return render(request, 'listing/detail.html', {
        'listing':listing,
        'related_listings': related_listings
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewListingForm (request.POST, request.FILES)
        if form.is_valid():
             Listing = form.save(commit=False)
             Listing.created_by = request.user
             Listing.save()


             return redirect('listing:detail', pk=Listing.id ) 
    
    else:
            form = NewListingForm()
    
    return render (request, 'listing/form.html', {
        'form': form,
        'title': 'New Listing',
    })
             
       
    

   
      