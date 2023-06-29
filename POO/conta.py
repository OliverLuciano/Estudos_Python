class Conta:
    
    def __init__(self, numero, titular, saldo, limite) :
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo 
        self.__limite = limite

    def extrato(self):
        print(f"O saldo da sua conta é de ${self.__saldo}")

    def deposito(self, valor):
        self.__saldo += valor
        return self.extrato()
    
    def saque(self, valor):
        self.__aldo -= valor
        return self.extrato()