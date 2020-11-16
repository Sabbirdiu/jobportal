
from django import forms
from .models import *

class CreateJobForm(forms.ModelForm):
    class Meta:
        model = JobListing
        exclude = ('user',)
       
        fields='__all__'
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'title'}),
            # 'category':forms.Select(attrs={'class':'form-control',}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'title'})
        }
      

    def is_valid(self):
        valid = super(CreateJobForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        job = super(CreateJobForm, self).save(commit=False)
        if commit:
            job.save()
        return job



class JobApplyForm(forms.ModelForm):
    class Meta:
        model = ApplyJob
        fields = '__all__'
        labels = {
            "file": "CV (pdf format)",
            "name": "Full Name"

        }
