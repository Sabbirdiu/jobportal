from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name='home'),
    path('joblist/',joblist, name='job' ),
    path('job-detail/<slug:slug>/',jobdetails, name='joblist' ),
    path('apply/', apply_job, name='apply'),
    path('employer/jobs/create', JobCreateView.as_view(), name='employer-jobs-create'),
] 