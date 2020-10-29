from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from django.http import HttpResponse
from home.models import Category,JobListing


def index(request):
    joblist = JobListing.objects.filter(featured=True)
    categories = Category.objects.filter()

    context = {
        'joblist': joblist,
        'categories':categories,
    }

    return render(request,"index.html",context)
def jobdetails(request,slug):
    joblist = get_object_or_404(JobListing, slug=slug)
    # joblist = JobListing.objects.all()
    
    context = {
        'joblists': joblist,
       
    }
    return render(request,"jobdetails.html",context)


