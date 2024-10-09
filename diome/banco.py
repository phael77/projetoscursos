class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R${valor:.2f} realizado com sucesso!')
        else:
            print('O valor do depósito deve ser positivo!')

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R${valor:.2f} realizado com sucesso!')
        else:
            print('Valor inválido para saque! Verifique seu saldo.')

    def visualizar_saldo(self):
        print(f'Saldo atual de {self.titular}: R${self.saldo:.2f}')


def main():
    print("Bem-vindo ao Sistema Bancário!")

    # Criar uma conta
    nome = input("Digite o nome do titular da conta: ")
    conta = ContaBancaria(nome)

    while True:
        print("\nEscolha uma opção:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Visualizar saldo")
        print("4. Sair")
        
        opcao = input("Opção: ")

        if opcao == '1':
            valor_deposito = float(input("Digite o valor a depositar: "))
            conta.depositar(valor_deposito)

        elif opcao == '2':
            valor_saque = float(input("Digite o valor a sacar: "))
            conta.sacar(valor_saque)

        elif opcao == '3':
            conta.visualizar_saldo()

        elif opcao == '4':
            print("Saindo do sistema. Obrigado!")
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
