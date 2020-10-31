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
def joblist(request):
    joblist = JobListing.objects.all()
    categories = Category.objects.filter()
    
    context = {
        'joblist': joblist,
        'categories':categories,
    }
    return render(request,"joblist.html",context)    


def jobdetails(request,slug):
    joblist = get_object_or_404(JobListing, slug=slug)
    otherjob = JobListing.objects.filter(featured=True).order_by('-published_on')[0:3]
    
    context = {
        'joblist': joblist,
        'otherjob':otherjob,
       
    }
    return render(request,"jobdetails.html",context)


