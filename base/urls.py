from django.urls import path
from .views import HomeView, QuemSomosView, CatequeseInfantilView, EucaristiaView, PerseverancaView, CrismaView, ProjetosView, EventosView, InscricoesView, InscricoesCatequizandosView, InscricoesCatequistasView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('quem-somos', QuemSomosView.as_view(), name='quem somos'),
    path('catequese-infantil', CatequeseInfantilView.as_view(), name='catequese infantil'),
    path('eucaristia', EucaristiaView.as_view(), name='eucaristia'),
    path('perseveranca', PerseverancaView.as_view(), name='perseveranca'),
    path('crisma', CrismaView.as_view(), name='crisma'),
    path('projetos', ProjetosView.as_view(), name='projetos'),
    path('eventos', EventosView.as_view(), name='eventos'),
    path('inscricoes', InscricoesView.as_view(), name='inscricoes'),
    path('inscricoes-catequizandos', InscricoesCatequizandosView.as_view(), name='inscricoes catequizandos'),
    path('inscricoes-catequistas', InscricoesCatequistasView.as_view(), name='inscricoes catequistas'),
]