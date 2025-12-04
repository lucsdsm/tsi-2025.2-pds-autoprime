from django.db import models

class Carro(models.Model):
    modelo = models.CharField(max_length=100, unique=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.modelo} - R$ {self.preco}"
    
    class Meta:
        db_table = 'carros'
        ordering = ['modelo']
