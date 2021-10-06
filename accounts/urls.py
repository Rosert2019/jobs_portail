from django.urls import path
from .views import *

urlpatterns = [ 
  path('signup/', sign_up.as_view(), name='signup'), #to sign up
]