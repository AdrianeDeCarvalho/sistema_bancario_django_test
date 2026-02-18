# 🏦 Sistema Bancário com Django & Testes Unitários

Este é um projeto de Back-end desenvolvido em Python/Django para consolidar conceitos de Lógica de Negócios e **Testes Unitários**.

## 🚀 Funcionalidades
- Criação de contas bancárias.
- Depósito e Saque com validações de segurança.
- Transferência entre contas.
- Registro automático de histórico (Extrato) para cada operação.

## 🧪 Testes Unitários (O Coração do Projeto)
O projeto foi desenvolvido utilizando a prática de testes para garantir a integridade das operações financeiras. Foram implementados testes de:
- Sucesso e falha em depósitos.
- Bloqueio de saques maiores que o saldo disponível.
- Integridade em transferências entre contas.
- Verificação da criação automática de registros no extrato.

Para rodar os testes:
```bash
python manage.py test```

🛠️

📋