from django.contrib import admin
from . models import Candidate, Company

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name','position', 'salary', 'experience', 'dep')
 
admin.site.register(Company, CompanyAdmin)

class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name','mobile', 'email', 'resume', 'company')

   # def get_position(self, obj):
        #we need to get for all applicants the postion that they had applied
       # return "\n".join([p.postion for p in obj.Company.all()])
 
admin.site.register(Candidate, CandidateAdmin)

