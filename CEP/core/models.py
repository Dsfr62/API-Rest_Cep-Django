from django.db import models

# Create your models here.

class loc(models.Model):
    # Registrar localizacao no db
    cep = models.TextField(max_length=20)
    endereco = models.TextField(max_length=100)
    numero = models.TextField(max_length=10)
    bairro = models.TextField(max_length=20)
    data_criacao = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Loc'

    def __str__(self):
        return self.cep