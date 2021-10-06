from django.urls import path
from .views import *

urlpatterns = [ 
    path('', home, name='home'),
    path('apply/',apply_view,name='apply'),
    path('add/',add_view,name='add'),
]