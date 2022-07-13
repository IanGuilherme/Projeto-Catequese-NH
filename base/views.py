from django.views.generic import TemplateView 

# Create your views here.

class HomeView(TemplateView):
    template_name= "home.html"

class QuemSomosView(TemplateView):
    template_name= 'QuemSomos.html'

class CatequeseInfantilView(TemplateView):
    template_name= 'CatequeseInfantil.html'

class EucaristiaView(TemplateView):
    template_name= 'Eucaristia.html'

class PerseverancaView(TemplateView):
    template_name= 'Perseveranca.html'

class CrismaView(TemplateView):
    template_name= 'Crisma.html'

class ProjetosView(TemplateView):
    template_name= 'Projetos.html'

class EventosView(TemplateView):
    template_name= 'Eventos.html'

class InscricoesView(TemplateView):
    template_name= 'Inscricoes.html'

class InscricoesCatequistasView(TemplateView):
    template_name= 'InscricoesCatequistas.html'

class InscricoesCatequizandosView(TemplateView):
    template_name= 'InscricoesCatequizandos.html'

