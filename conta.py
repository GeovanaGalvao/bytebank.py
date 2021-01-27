
class Conta:

    def __init__(self, numero, titular, saldo=100.0, limite=1000.0):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("\nO saldo de {} é de R$:{} .".format(self.__titular, self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor if valor > 0.0 else print("\nNão é possível depositar esse valor.")

    def saca(self, valor):
        if self.__saldo >= valor > 0.0:
            self.__saldo -= valor
            return valor
        else:
            print("\nSaldo na conta insuficiente para realizar a ação desejada.")
            return 0.0

    def transfere(self, conta, valor):
        conta.deposita(valor) if self.saca(valor) != 0.0 else None
        # Se o retorno do metodo saca for maior do que 0.0 , realiza o depósito do valor sacado na outra conta.
