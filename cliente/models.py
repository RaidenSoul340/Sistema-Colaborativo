from django.db import models

class User(models.Model):
    id = models.BigAutoField(primary_key=True)  # Adicionando uma chave primária explícita
    Nome = models.CharField(max_length=100)
    Email = models.EmailField()
    Senha = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Nome

class Task(models.Model):
    id = models.BigAutoField(primary_key=True)  # Adicionando uma chave primária explícita
    Titulo = models.CharField(max_length=80)
    Descricao = models.TextField()
    Data_Criacao = models.DateTimeField(auto_now_add=True)
    Data_Limite = models.DateTimeField(null=True)
    Status = models.BooleanField(default=False)
    Atribuido = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Titulo
