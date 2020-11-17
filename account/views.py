from django.shortcuts import render

# Create your views here.

from django.contrib import messages, auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView, RedirectView,UpdateView
from account.forms import *
from account.models import User
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from .decorators import user_is_employee
# def signup(request):
#     return render(request,'signup.html')
class RegisterEmployeeView(CreateView):
    model = User
    form_class = EmployeeRegistrationForm
    template_name = 'signup.html'
    success_url = '/signin'

    # extra_context = {
    #     'title': 'signup'
    # }

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get("password1")
            user.set_password(password)
            user.save()
            return redirect('/signin')
        else:
            return render(request, 'signup.html', {'form': form})    

# def signin(request):
#     return render(request,'signin.html')
class RegisterEmployerView(CreateView):
    model = User
    form_class = EmployerRegistrationForm
    template_name = 'employersignup.html'
    success_url = '/signin'

    # extra_context = {
    #     'title': 'signup'
    # }

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get("password1")
            user.set_password(password)
            user.save()
            return redirect('/signin')
        else:
            return render(request, 'employersignup.html', {'form': form})


class signin(FormView):
    """
        Provides the ability to login as a user with an email and password
    """
    success_url = '/dashboard'
    form_class = UserLoginForm
    template_name = 'signin.html'

    extra_context = {
        'title': 'signin'
    }

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)

    def get_success_url(self):
        if 'next' in self.request.GET and self.request.GET['next'] != '':
            return self.request.GET['next']
        else:
            return self.success_url

    def get_form_class(self):
        return self.form_class

    def form_valid(self, form):
        auth.login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return self.render_to_response(self.get_context_data(form=form))



def employersignup(request):
    return render(request,'employersignup.html')
class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = '/signin'

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return super(LogoutView, self).get(request, *args, **kwargs)
def dashboard(request):
    return render(request,'profile/dashboard_profile.html')

    
def employeerdashboard(request):
    return render(request,'employeer/dashboard_profile.html')

class EditProfileView(UpdateView):
    model = User
    form_class = EmployeeProfileUpdateForm
    context_object_name = 'employee' 
    template_name = 'profile/edit-profile.html'
    success_url = reverse_lazy('employer-profile-update')

    @method_decorator(login_required(login_url=reverse_lazy('signin')))
    @method_decorator(user_is_employee)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            raise Http404("User doesn't exists")
        # context = self.get_context_data(object=self.object)
        return self.render_to_response(self.get_context_data())

    def get_object(self, queryset=None):
        obj = self.request.user
        print(obj)
        if obj is None:
            raise Http404("Job doesn't exists")
        return obj

        