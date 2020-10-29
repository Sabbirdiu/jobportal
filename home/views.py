from django.shortcuts import render
from django.http import HttpResponse
from home.models import Category,JobListing


def index(request):
    qs = JobListing.objects.all()

    context = {
        'joblist': qs,
    }

    return render(request,"index.html",context)