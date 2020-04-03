#librerias de funcinamiento
from django.urls import include,re_path,path
from django.conf import settings 
from . import views 
#importar las vistas de la pagina
from Dashboard.views import DashboardClass
#invocar aplicacion 
app_name = 'Dashboard'

#llamo las url que va a tener cada html en las hijas
urlpatterns = [
   path('',DashboardClass.as_view(),name='Dashboard'),
]