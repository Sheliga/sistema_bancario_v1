# sistema_bancario.py
from datetime import datetime


def agora() -> str:
    """Retorna timestamp formatado."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def log(msg: str):
    """Exibe mensagens sempre com timestamp."""
    print(f"[{agora()}] {msg}")


def formatar_valor(valor: float) -> str:
    """Formata o valor no padrão brasileiro R$ 0,00."""
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def ler_valor(mensagem: str) -> float:
    """Lê um valor numérico válido do usuário."""
    while True:
        entrada = input(mensagem)
        try:
            valor = float(entrada.replace(",", "."))
            return valor
        except ValueError:
            log("Entrada inválida! Digite um número válido.")


def main():
    saldo = 0.0
    limite = 500.0
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        print("\n=== SISTEMA BANCÁRIO ===")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Extrato")
        print("4 - Saldo")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = ler_valor("Informe o valor do depósito: R$ ")
            if valor <= 0:
                log("Operação falhou! O valor do depósito deve ser positivo.")
            else:
                saldo += valor
                extrato.append(f"[{agora()}] Depósito: {formatar_valor(valor)}")
                log(f"Depósito de {formatar_valor(valor)} realizado com sucesso.")

        elif opcao == "2":
            valor = ler_valor("Informe o valor do saque: R$ ")

            if valor <= 0:
                log("Operação falhou! O valor do saque deve ser positivo.")
            elif valor > saldo:
                log("Operação falhou! Saldo insuficiente.")
            elif valor > limite:
                log(
                    f"Operação falhou! O valor máximo por saque é {formatar_valor(limite)}."
                )
            elif numero_saques >= LIMITE_SAQUES:
                log("Operação falhou! Número máximo de saques diários atingido.")
            else:
                saldo -= valor
                extrato.append(f"[{agora()}] Saque: {formatar_valor(valor)}")
                numero_saques += 1
                log(f"Saque de {formatar_valor(valor)} realizado com sucesso.")

        elif opcao == "3":
            print("\n=== EXTRATO ===")
            if not extrato:
                log("Não foram realizadas movimentações.")
            else:
                for mov in extrato:
                    print(mov)
            print(f"\nSaldo atual: {formatar_valor(saldo)}")

        elif opcao == "4":
            log(f"Saldo atual: {formatar_valor(saldo)}")

        elif opcao == "0":
            log("Saindo do sistema bancário...")
            break

        else:
            log("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
