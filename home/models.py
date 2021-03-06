from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import get_user_model
from account.models import User

class Category(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(null=True)
    image = models.ImageField(blank=True, upload_to='media', null=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('joblist_in_category', kwargs={
            'slug': self.slug
        })
    
    def save(self, *args, **kwargs):
        if self.title:
            self.title = self.title.capitalize()

        super(Category, self).save(*args, **kwargs) 
JOB_TYPE = (
    ('Part Time', 'Part Time'),
    ('Full Time', 'Full Time'),
    ('Freelance', 'Freelancer'),
)

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Any', 'Any'),
)
QALIFICATION = (
    ('Honours','Honours'),
    ('Masters','Masters'),

)

class JobListing(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             null=True, editable=False, blank=True)
    category = models.ManyToManyField(Category)                         
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    company_name = models.CharField(max_length=200)
    employment_status = models.CharField(choices=JOB_TYPE, max_length=10)
    vacancy = models.CharField(max_length=10, null=True)
    gender = models.CharField(choices=GENDER, max_length=30, null=True)
    description = models.TextField()
    responsibilities = models.TextField()
    experience = models.CharField(max_length=100)
    job_location = models.CharField(max_length=120)
    Salary = models.CharField(max_length=100, null=True, blank=True)
    qualification=models.CharField(choices=QALIFICATION, max_length=30, null=True,blank=True)
    image = models.ImageField(blank=True, upload_to='media', null=True, default='/static/extra-images/employer-2.png')
    application_deadline = models.DateTimeField()
    published_on = models.DateTimeField(default=timezone.now)
    featured = models.BooleanField()

    def __str__(self):
        return self.title
    def get_absolute_url(self):
            return reverse('joblist', kwargs={
                'slug': self.slug
            })    
    @property
    def get_photo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/static/extra-images/employer-2.png"        

class ApplyJob(models.Model): 
    name = models.CharField(max_length=50)
    email = models.EmailField()
    file = models.FileField(null=True)

    def __str__(self):
        return self.name



class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(JobListing, on_delete=models.CASCADE, related_name="favorites")
    created_at = models.DateTimeField(default=timezone.now)
    soft_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.job.title
