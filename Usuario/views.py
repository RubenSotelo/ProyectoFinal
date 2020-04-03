from django.shortcuts import render
#librerias de funcionamiento 
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib.auth import authenticate

#accion que tiene la vista se tienen en la vista con cada archivo html
    #crear una clase para la vista
class UsuarioClass(View):
    URL='Usuario/usuario.html'
    def get(self,request,*args,**kwargs):
        # retorno la direcion de la carpeta para cada html
        return render(request,self.URL,{}) 
    def post(self,request,*args,**kwargs):
        # me redirigo en la urls de dashboard
        return redirect('Dashboard:Dashboard')