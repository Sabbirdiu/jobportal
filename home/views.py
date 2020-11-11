from django.shortcuts import render,get_object_or_404,HttpResponseRedirect,redirect
from django.http import HttpResponse
from home.models import Category,JobListing,ApplyJob
from django.contrib.auth.decorators import login_required
from .forms import *


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
@login_required(login_url='/signin')
def apply_job(request):
    form = JobApplyForm(request.POST or None, request.FILES)
    if form.is_valid():
        instance = form.save()
        instance.save() 
        return redirect('/')
        
    context = {
        'form': form,

    } 
    return render(request, "jobs/job_apply.html", context)

