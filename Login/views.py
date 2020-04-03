from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.views.generic.edit import FormView
from Registro.forms import RegisterBusinessForm
class LoginClass(View):
    URL='Login/login.html'
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('Dashboard:Dashboard')
        return render(request,self.URL,{}) 
    def post(self,request,*args,**kwargs):
        user = request.POST['user']
        password = request.POST['password']
        Inicio = authenticate(username =user, password = password)
        if Inicio is not None:
            login_django(request,Inicio)
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('Dashboard:Dashboard')
        else:
            self.messege = 'no existe ese usuario o contraseña'
            
        return render(request,self.URL,self.get_context())

    def get_context(self):
        return{
            'error':self.messege
        } 

    
