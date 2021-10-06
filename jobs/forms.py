from django.forms import ModelForm
from .models import Candidate, Company


#form for job seekers
class apply_form(ModelForm):

    class Meta:
        model=Candidate
        fields=['name', 'birth_date','gender','mobile','email','resume','company']


class add_job(ModelForm):
    class Meta:
        model= Company
        fields= ['name', 'position', 'description','salary', 'experience', 'dep']        

