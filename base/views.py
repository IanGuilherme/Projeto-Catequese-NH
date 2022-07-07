from django.views.generic import TemplateView 

# Create your views here.

class HomeView(TemplateView):
    template_name= "home.html"

class QuemSomosView(TemplateView):
    template_name = 'QuemSomos.html'