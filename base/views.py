from django.shortcuts import render
from .models import Table

# Create your views here.
def home(request):
    return render(request, 'base/index.html')

def login(request):
    return render(request, 'base/login.html')

def form(request):
    return render(request, 'base/form.html')
    
def dashboard(request):
    tab = Table.objects.all()
    return render(request, 'base/dashboard.html',{'tab': tab})
