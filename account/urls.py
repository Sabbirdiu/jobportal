from django.urls import path
from .views import *


urlpatterns = [
    # path('signup/',signup,name='signup'),
    path('employee/register/', RegisterEmployeeView.as_view(), name='signup'),
    path('employer/register', RegisterEmployerView.as_view(), name='employersignup'),
    # path('signin/',signin,name='signin'),
    path('signin', signin.as_view(), name='signin'),
    # path('employersignup/',employersignup,name='employersignup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    
]