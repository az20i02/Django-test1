from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import LoginForm

urlpatterns = [
    path('index/', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.Signup, name='Signup'),
    path('login/', auth_views.LoginView.as_view(template_name='pages/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),



    
    # for user info page
    path('logged_user/', views.logged_user, name='logged_user'),
]

