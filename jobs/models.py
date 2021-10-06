from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Company(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=200, verbose_name='Company name')
    position=models.CharField(max_length=200, verbose_name='Position title')
    description=models.CharField(max_length=2500, verbose_name='Job description')
    salary=models.FloatField()
    experience=models.FloatField(verbose_name='Number of year experiences')
    dep=models.CharField(max_length=2, verbose_name='Departement')

    class Meta:
        verbose_name_plural = "Compagnies"

    def __str__(self):
        return self.name


class Candidate(models.Model):
    category=(
        ('Male','male'),
        ('Female','female'),
      
    )
    name=models.CharField(max_length=200, verbose_name='Candidate name')
    birth_date=models.DateField(verbose_name='Date of birth')
    gender= models.CharField(max_length=200, choices=category)
    mobile= models.CharField(max_length=200)
    email= models.EmailField()
    resume=models.FileField(verbose_name='CV')
    company=models.ForeignKey(Company, on_delete=models.CASCADE)


    def __str__(self):
        return self.name        

    #get of candidate from date of birth  
    def get_age(self):
        return int((datetime.now().date() - self.birth_date).days / 365.25)
      