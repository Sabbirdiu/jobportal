from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name='home'),
    path('job-detail/<slug:slug>/',jobdetails, name='joblist' ),
]