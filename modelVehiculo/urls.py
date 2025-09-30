from django.urls import path
from . import views

app_name = 'vehiculos'

urlpatterns = [
    # CREATE - Agregar nuevo vehículo
    path('', views.index, name='agregar'),
    
    path('listar/', views.listar_vehiculo, name='listar'),
    
    path('buscar/<int:id>/', views.buscar_vehiculo, name='detalle'),
    
    path('editar/<int:id>/', views.editar_vehiculo, name='editar'),
    
    path('eliminar/<int:id>/', views.eliminar_vehiculo, name='eliminar'),
]