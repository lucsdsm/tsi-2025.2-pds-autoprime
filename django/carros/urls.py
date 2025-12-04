from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getCarro', views.get_carro, name='get_carro'),
    path('saveCarro', views.save_carro, name='save_carro'),
    path('deleteCarro', views.delete_carro, name='delete_carro'),
    path('updateCarro', views.update_carro, name='update_carro'),
    path('listarCarros', views.listar_carros, name='listar_carros'),
]
