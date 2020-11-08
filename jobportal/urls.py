from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

from account import views as acviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('',include('account.urls')),



    # path('signup/',signup,name='signup'),
    # path('employee/register/', RegisterEmployeeView.as_view(), name='signup'),
    # # path('signin/',signin,name='signin'),
    # path('signin', signin.as_view(), name='signin'),
    # path('employersignup/',acviews.employersignup,name='employersignup'),
    # path('logout/', LogoutView.as_view(), name='logout'),



]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
