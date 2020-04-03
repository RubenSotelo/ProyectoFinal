from django.shortcuts import render
#librerias de funcionamiento 
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth import login as login_django
#accion que tiene la vista se tienen en la vista con cada archivo html
    #crear una clase para la vista
class DashboardClass(View):
    URL='Dashboard/dashboard.html'
    def get(self,request,*args,**kwargs):
        urls="{% static "+"'imagenes/icono.png'"+" %}"
        return render(request,self.URL,{'url':urls}) 

    def post(self,request,*args,**kwargs):
        logout(request)
        return redirect('Login:Login')
        
        # me redirigo en la urls de dashboard
        