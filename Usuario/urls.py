#librerias de funcinamiento
from django.urls import include,re_path,path
from django.conf import settings 
from . import views 
#importar las vistas de la pagina
from Usuario.views import UsuarioClass
#invocar aplicacion 
app_name = 'Usuario'

#llamo las url que va a tener cada html en las hijas
urlpatterns = [
   path('',UsuarioClass.as_view(),name='Usuario'),
]