from django.db import models

class Tutor(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['nome']
        verbose_name = 'Tutor'
        verbose_name_plural = 'Tutores'