#librerias de funcinamiento
from django.urls import include,re_path,path
from django.conf import settings 
from . import views 
#importar las vistas de la pagina
from Landing.views import LandingClass
#invocar aplicacion 
app_name = 'Landing'

#llamo las url que va a tener cada html en las hijas
urlpatterns = [
   path('',LandingClass.as_view(),name='Landing'),
]