from django.db import models

# Create your models here.
class Conta(models.Model):
    titular = models.CharField(max_length=100)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.save()
            Transacao.objects.create(conta=self, tipo='D', valor=valor)
            return True
        return False
    
    def sacar(self, valor):
        if 0 <  valor <= self.saldo:
            self.saldo -= valor
            Transacao.objects.create(conta=self, tipo='S', valor=valor)
            self.save()
            return True
        return False
    
    def __str__(self):
        return f"Conta de {self.titular} - Saldo: R$ {self.saldo}"
    
    def transferir(self, conta_destino, valor):
        if self.sacar(valor):
            conta_destino.depositar(valor)
            return True
        return False
    

class Transacao(models.Model):
    TIPOS = (
        ('D', 'Depósito'),
        ('S', 'Sacar'),
        ('T', 'Transferência'),
    )

    conta = models.ForeignKey(Conta, on_delete=models.CASCADE, related_name='transacoes')
    tipo = models.CharField(max_length=1, choices=TIPOS)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_tipo_display()} - R$ {self.valor} em {self.data}"
