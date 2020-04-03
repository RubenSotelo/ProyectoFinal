#librerias de funcinamiento
from django.urls import include,re_path,path
from django.conf import settings 
from . import views 
#importar las vistas de la pagina
from Registro.views import RegistroClass

#invocar aplicacion 
app_name = 'Registro'

#llamo las url que va a tener cada html en las hijas
urlpatterns = [
   path('',RegistroClass.as_view(),name='Registro'),
]