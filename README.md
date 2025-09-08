
# Sistema Bancário em Python (CLI)

Este projeto implementa um **sistema bancário simples em Python** que roda no **terminal (CLI)**.
Ele permite realizar **depósitos, saques, consultar saldo e extrato**, respeitando regras de negócio comuns em operações bancárias.

---

## Funcionalidades

- **Depósito**

  - Apenas valores positivos.
  - Saldo atualizado imediatamente.
- **Saque**

  - Máximo de **3 saques por dia**.
  - Limite de **R$ 500,00 por saque**.
  - Não permite sacar mais do que o saldo disponível.
- **Extrato**

  - Lista todas as movimentações com **timestamp**.
  - Mostra o saldo final no momento da consulta.
- **Saldo**

  - Exibe apenas o saldo atual, sem precisar mostrar o extrato completo.
- **Validações**

  - Impede depósito ou saque de valores inválidos (zero, negativos ou não numéricos).
  - Exibe mensagens sempre com **timestamp**.

---

## Estrutura do Projeto
