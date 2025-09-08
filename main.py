# sistema_bancario_poo.py
from datetime import datetime


def agora() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def formatar_valor(valor: float) -> str:
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


class ContaBancaria:
    LIMITE_SAQUES = 3
    LIMITE_VALOR = 500.0

    def __init__(self, numero: int, cliente: "Cliente"):
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0.0
        self.extrato = []
        self.numero_saques = 0
        self.limite = ContaBancaria.LIMITE_VALOR

    def depositar(self, valor: float):
        if valor <= 0:
            print(
                f"[{agora()}] Operação falhou! O valor do depósito deve ser positivo."
            )
            return
        self.saldo += valor
        self.extrato.append(f"[{agora()}] Depósito: {formatar_valor(valor)}")
        print(f"[{agora()}] Depósito de {formatar_valor(valor)} realizado com sucesso.")

    def sacar(self, valor: float):
        if valor <= 0:
            print(f"[{agora()}] Operação falhou! O valor do saque deve ser positivo.")
        elif valor > self.saldo:
            print(f"[{agora()}] Operação falhou! Saldo insuficiente.")
        elif valor > self.limite:
            print(
                f"[{agora()}] Operação falhou! O valor máximo por saque é {formatar_valor(self.limite)}."
            )
        elif self.numero_saques >= ContaBancaria.LIMITE_SAQUES:
            print(
                f"[{agora()}] Operação falhou! Número máximo de saques diários atingido."
            )
        else:
            self.saldo -= valor
            self.extrato.append(f"[{agora()}] Saque: {formatar_valor(valor)}")
            self.numero_saques += 1
            print(
                f"[{agora()}] Saque de {formatar_valor(valor)} realizado com sucesso."
            )

    def mostrar_extrato(self):
        print("\n=== EXTRATO ===")
        if not self.extrato:
            print(f"[{agora()}] Não foram realizadas movimentações.")
        else:
            for mov in self.extrato:
                print(mov)
        print(f"\nSaldo atual: {formatar_valor(self.saldo)}")

    def mostrar_saldo(self):
        print(f"[{agora()}] Saldo atual: {formatar_valor(self.saldo)}")


class Cliente:
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf
        self.contas = []

    def adicionar_conta(self, conta: ContaBancaria):
        self.contas.append(conta)

    def __str__(self):
        return f"Cliente: {self.nome} - CPF: {self.cpf}"


# ------------------------
# Programa principal
# ------------------------


def main():
    # Criando um cliente de exemplo
    cliente = Cliente("João Silva", "123.456.789-00")
    conta = ContaBancaria(1, cliente)
    cliente.adicionar_conta(conta)

    while True:
        print("\n=== SISTEMA BANCÁRIO ===")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Extrato")
        print("4 - Saldo")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                valor = float(
                    input("Informe o valor do depósito: R$ ").replace(",", ".")
                )
                conta.depositar(valor)
            except ValueError:
                print(f"[{agora()}] Entrada inválida! Digite um número válido.")

        elif opcao == "2":
            try:
                valor = float(input("Informe o valor do saque: R$ ").replace(",", "."))
                conta.sacar(valor)
            except ValueError:
                print(f"[{agora()}] Entrada inválida! Digite um número válido.")

        elif opcao == "3":
            conta.mostrar_extrato()

        elif opcao == "4":
            conta.mostrar_saldo()

        elif opcao == "0":
            print(f"[{agora()}] Saindo do sistema bancário...")
            break

        else:
            print(f"[{agora()}] Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
