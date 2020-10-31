from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name='home'),
    path('joblist/',joblist, name='job' ),
    path('job-detail/<slug:slug>/',jobdetails, name='joblist' ),
]