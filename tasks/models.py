from django.db import models
from  django.contrib.auth import get_user_model

# Create your models here.

class Task(models.Model):

    STATUS = (
        ('doing', 'Doing'),
        ('done', 'Done')
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(
        max_length=5,
        choices=STATUS,
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) # Data de quando o registro foi criado (dia,mês, ano e hr) - sempre que criar um registro cria um valor de data no banco
    updated_at = models.DateTimeField(auto_now=True) # Atualiza a data quando é feita uma nova atualização no banco

    def __str__(self):
        return self.title