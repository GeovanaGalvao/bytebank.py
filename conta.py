
class Conta:

    def __init__(self, numero, titular, saldo=100.0, limite=500.0, codigo_banco="001"):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = codigo_banco

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @property
    def codigo_banco(self):
        return self.__codigo_banco

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigos_bancos():
        return {"Banco do Brasil": "001", "Caixa": "104", "Bradesco": "237"}

    def extrato(self):
        print("\nO saldo de {} é de R$:{} reais.".format(self.titular, self.saldo))

    def deposita(self, valor):
        self.__saldo += valor if valor > 0.0 else print("\nNão é possível depositar esse valor.")

    def saca(self, valor_desejado):
        if self.__verifica_possibilidade_de_saque(valor_desejado):
            self.__saldo -= valor_desejado
            return valor_desejado
        else:
            print("\nSaldo na conta insuficiente para realizar a ação desejada.")
            return 0.0

    def transfere(self, conta, valor):
        conta.deposita(valor) if self.saca(valor) != 0.0 else None
        # Se o retorno do metodo saca for maior do que 0.0 , realiza o depósito do valor sacado na outra conta.

    def __verifica_possibilidade_de_saque(self, valor_a_sacar):
        return self.saldo + self.limite >= valor_a_sacar
