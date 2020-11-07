from django.shortcuts import render

# Create your views here.

from django.contrib import messages, auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView, RedirectView
from account.forms import *
from account.models import User

# def signup(request):
#     return render(request,'signup.html')
class RegisterEmployeeView(CreateView):
    model = User
    form_class = EmployeeRegistrationForm
    template_name = 'signup.html'
    success_url = '/'

    extra_context = {
        'title': 'signup'
    }

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
            return redirect('account:signin')
        else:
            return render(request, 'signup.html', {'form': form})    

def signin(request):
    return render(request,'signin.html')

def employersignup(request):
    return render(request,'employersignup.html')
