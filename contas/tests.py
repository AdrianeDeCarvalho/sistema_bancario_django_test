from django.test import TestCase
from .models import Conta

# Create your tests here.
class ContaModelTest(TestCase):
    def setUp(self):
        self.conta = Conta.objects.create(titular='Adriane', saldo=100.00)

    def test_deposito_valor(self):
        sucesso = self.conta.depositar(50.00)
        self.assertTrue(sucesso)
        self.assertEqual(self.conta.saldo, 150.00)

    def test_saque_insuficiente(self):
        sucesso = self.conta.sacar(200.00)
        self.assertFalse(sucesso)
        self.assertEqual(self.conta.saldo, 100.00)

    def test_valor_negativo(self):
        sucesso = self.conta.depositar(-10.00)
        self.assertFalse(sucesso)
        self.assertEqual(self.conta.saldo, 100.00)

    def test_transferencia_entre_contas(self):
        conta_recebedora = Conta.objects.create(titular='Joao', saldo=50.00)
        sucesso = self.conta.transferir(conta_recebedora, 30.00)

        self.assertTrue(sucesso)
        self.assertEqual(self.conta.saldo, 70.00)
        self.assertEqual(conta_recebedora.saldo, 80.00)

    def test_historico_transacao_criado(self):
        self.conta.depositar(50.00)
        self.conta.sacar(20.00)

        quantidade = self.conta.transacoes.count()
        self.assertEqual(quantidade, 2)

    def test_detalhe_do_extrato(self):
        self.conta.depositar(100.00)

        ultima_transacao = self.conta.transacoes.last()

        self.assertEqual(ultima_transacao.tipo, 'D')
        self.assertEqual(ultima_transacao.valor, 100.00)

