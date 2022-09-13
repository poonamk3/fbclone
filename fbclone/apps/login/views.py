from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm  
from .forms import SignupForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.views.generic import TemplateView
def index(request):
	return render(request,"enroll/home.html")
class HomeView(TemplateView):
    template_name='enroll/homehtml.html'
class RegisterView(CreateView):
    form_class = SignupForm
    template_name='enroll/index.html'
    success_url = '/home/'

class ProfileView(TemplateView):
    template_name='enroll/proflie.html'
    
