from django.urls import path
from .views import *
urlpatterns = [
    path('signup/',signup,name='signup'),
    path('signin/',signin,name='signin'),
    path('employersignup/',employersignup,name='employersignup'),
    
]