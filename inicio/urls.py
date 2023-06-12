from django.urls import path
from . import views
app_name = 'info_app'
urlpatterns = [
    path('', views.inicio),
    path('login_admin', views.gestion),
    path('matricula', views.matricula, name='matricula'),
    path('crear_matricula', views.CrearMatricula.as_view(), name='crear_matricula'),
    path('egreso', views.egreso, name='egreso'),
    path('logout', views.logout_view),
    path('resumenes', views.resumenes),
    path('opcion', views.opcion),
    path('matriculados', views.matriculados),
    path('egresados', views.egresados),
    path('graficos', views.grafico),

    path('guardar-matricula/', views.guardar_matricula, name='guardar_matricula'),
    path('modificar-matricula/<int:pk>/', views.modificar_matricula, name='modificar_matricula'),
    path('eliminar_matricula/<int:pk>/', views.eliminar_matricula, name='eliminar_matricula'),

    path('guardar-egreso/', views.guardar_egreso, name='guardar_egreso'),
    path('modificar-egreso/<int:pk>/', views.modificar_egreso, name='modificar_egreso'),
    path('crear_egreso', views.CrearEgreso.as_view(), name='crear_egreso'),
    path('eliminar_egreso/<int:pk>/', views.eliminar_egreso, name='eliminar_egreso'),
]