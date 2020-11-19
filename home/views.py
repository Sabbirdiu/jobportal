from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404, HttpResponseRedirect, JsonResponse
from home.models import Category,JobListing,ApplyJob
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView
from django.utils.decorators import method_decorator
from .forms import *
from account.decorators import user_is_employee,user_is_employer

def index(request):
    joblist = JobListing.objects.filter(featured=True)
    categories = Category.objects.filter()

    context = {
        'joblist': joblist,
        'categories':categories,
    }

    return render(request,"index.html",context)
def joblist(request):
    joblist = JobListing.objects.all()
    categories = Category.objects.filter()
    
    context = {
        'joblist': joblist,
        'categories':categories,
    }
    return render(request,"joblist.html",context)    


def jobdetails(request,slug):
    joblist = get_object_or_404(JobListing, slug=slug)
    otherjob = JobListing.objects.filter(featured=True).order_by('-published_on')[0:3]
    
    context = {
        'joblist': joblist,
        'otherjob':otherjob,
       
    }
    return render(request,"jobdetails.html",context)
@login_required(login_url='/signin')
def apply_job(request):
    form = JobApplyForm(request.POST or None, request.FILES)
    if form.is_valid():
        instance = form.save()
        instance.save() 
        return redirect('/')
        
    context = {
        'form': form,

    } 
    return render(request, "jobs/job_apply.html", context)

class JobCreateView(CreateView):
    template_name = 'jobs/create.html'
    form_class = CreateJobForm
    # model = JobListing
    # fields='__all__'
    extra_context = {
        'title': 'Post New Job'
    }
    success_url = reverse_lazy('employeerdashboard')

    @method_decorator(login_required(login_url=reverse_lazy('signin')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('signin')
        if self.request.user.is_authenticated and self.request.user.role != 'employer':
            return reverse_lazy('signin')
        return super().dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(JobCreateView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

@method_decorator(login_required(login_url=reverse_lazy('/signin')), name='dispatch')
@method_decorator(user_is_employee, name='dispatch')
class FavoriteListView(ListView):
    model = Favorite
    template_name = "profile/favorites.html"
    context_object_name = "favorites"

    def get_queryset(self): 
        return self.model.objects.select_related('job__user').filter(soft_deleted=False, user=self.request.user)
def favorite(request):
    if not request.user.is_authenticated:
        return JsonResponse(data={"auth": False, "status": "error"})

    job_id = request.POST.get('job_id')
    user_id = request.user.id
    try:
        fav = Favorite.objects.get(job_id=job_id, user_id=user_id, soft_deleted=False)
        if fav:
            fav.soft_deleted = True
            fav.save()
            # fav.delete()
            return JsonResponse(data={"auth": True, "status": "removed", "message": "Job removed from your favorite list"})
    except Favorite.DoesNotExist:
        Favorite.objects.create(job_id=job_id, user_id=user_id)
        return JsonResponse(data={"auth": True, "status": "added", "message": "Job added to your favorite list"})

