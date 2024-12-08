from django.db import models

class User(models.Model):
    Nome = models.CharField(max_length=100)
    Email = models.EmailField()
    Senha = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Nome

class Task(models.Model):
    Titulo = models.CharField(max_length=80)
    Descricao = models.TextField()
    Data_Criacao = models.DateTimeField(auto_now_add=True)
    Data_Limite = models.DateTimeField()
    Status = models.BooleanField(default=False)
    Atribuido = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Titulo