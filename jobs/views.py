from django.shortcuts import render, redirect
from .models import Candidate, Company
from .forms import apply_form, add_job


# Create your views here.


# It filters all the candidates, applied to HR’s organization, and passes them to the hr.html file, which displays all the candidates in tabular form and also provides an option to download their resumes
def home(request):
    if request.user.is_authenticated:
        candidates=Candidate.objects.filter(company__name=request.user.username)
        context={
            'candidates':candidates,
        }
        return render(request,'jobs/hr.html',context)
    else:
        companies=Company.objects.all()
        context={
            'companies':companies,
        }
        return render(request,'jobs/jobseeker.html',context)



#form to apply for candidates
def apply_view(request):
    form=apply_form()
    if request.method=='POST':
        form=apply_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'jobs/add_job.html',context)


#add a new job   
def add_view(request):
    if request.user.is_authenticated:
        form=add_job()  
        if request.method=='POST':
           form=add_job(request.POST)
           if form.is_valid():
               form.save()
               return redirect('home')
        context={'form':form}
        return render(request,'jobs/add_job.html',context)
    else:
        return redirect('home')   