#tendra todas las url del sitio web
from django.contrib import admin
from django.urls import path,include
from .views import home,galeria,formulario,quienes_somos,formulario2,eliminar_pelicula,login,login_iniciar

urlpatterns = [
    path('',home,name='HOME'),
    path('galeria/',galeria,name='GALE'),
    path('formulario/',formulario2,name='FORMU'),
    path('quienes_somos/',quienes_somos,name='QUIEN'),
    path('eliminar_pelicula/<id>/',eliminar_pelicula,name='ELIMINAR')  ,
    path('login/',login,name='LOGIN'),
    path('login_iniciar/',login_iniciar,name="LOGIN_INICIAR"),
]