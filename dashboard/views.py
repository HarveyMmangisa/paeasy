from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from listing.models import Listing

@login_required
def index(request):
  listings = Listing.objects.filter(created_by=request.user)

  return render ( request, 'dashboard/index.html',{
      'listings': listings,
  })