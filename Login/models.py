from django.db import models
class Usuario(models.Model):    
    nombreUsuario=models.CharField(max_length=254,null=False)
    usuario=models.CharField(max_length=254,null=False)
    password=models.CharField(max_length=254,null=False)
    correo=models.CharField(max_length=254,null=False)
    def __str__(self):
        return 'en nombre es '+ self.nombreUsuario