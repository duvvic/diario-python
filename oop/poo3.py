class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0.0):
        self._titular = titular          
        self._saldo = saldo_inicial      

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido. Deve ser maior que zero.")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque inválido. Deve ser maior que zero.")
        elif valor > self._saldo:
            print("Saldo insuficiente para realizar o saque.")
        else:
            self._saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")

    def exibir_saldo(self):
        print(f"Titular: {self._titular} | Saldo atual: R${self._saldo:.2f}")


conta = ContaBancaria("Victor", 1000)
conta.exibir_saldo()
conta.depositar(500)
conta.sacar(300)
conta.sacar(1500)  
conta.exibir_saldo()
