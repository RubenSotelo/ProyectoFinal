#librerias de funcinamiento
from django.urls import include,re_path,path
from django.conf import settings 
from . import views 
#importar las vistas de la pagina
from Login.views import LoginClass

#invocar aplicacion 
app_name = 'Login'

#llamo las url que va a tener cada html en las hijas
urlpatterns = [
   path('',LoginClass.as_view(),name='Login'),
]