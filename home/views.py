from django.shortcuts import render
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