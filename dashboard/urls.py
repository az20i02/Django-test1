from django.urls import path
from . import views


app_name = 'dashboard'
urlpatterns = [
    path('indexDash/', views.indexDash, name='indexDash'),
    
   
]