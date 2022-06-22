#from django.shortcuts import render
#from django.http import HttpResponse
from django.views.generic import TemplateView 

# Create your views here.
'''
def view_home(request):
    return HttpResponse('Página home')

def view_home(request):
    return render(request, "home.html")'''

class HomeView(TemplateView):
    template_name= "home.html"