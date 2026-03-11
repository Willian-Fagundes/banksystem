from abc import ABC, classmethod
from datetime import datetime
class Cliente():
    
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    
    def transacao(self, conta, transacao):
        transacao.registrar(conta)

    def add_conta(self,conta):
        self.contas.append(conta)

class PessoaFisisca(Cliente):

    def __init__(self, nome, data_nasc, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nasc = data_nasc
        self.cpf = cpf

class Conta():
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "00001"
        self._cliente = cliente
        self._historico - Historico()
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self._saldo
        exede_saldo = valor > saldo

        if exede_saldo:
            print("Operação negada, saldo insuficiente")
        
        elif valor > 0:
            self._saldo -= valor
            print("Saque realizado")
            return True
        
        else:
            print("Valor Invalido")

            return False
        
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Deposito feito")
        else:
            print("valor invalido")        
    
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite = 500, limite_saques = 3):
        super().__init__(numero, cliente)
        self._limite_saque = limite_saques
        self._limite = limite

    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacao if transacao["tipo"] == Saque.__name__])
        exede_limite = valor > self._limite
        exede_saques = numero_saques > self._limite_saque

        if exede_limite:
            print ("Limite de valor excedido")
        elif exede_saques:
            print("Limite de saques excedido")
        
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""\
                Agencia:\t{self.agencia}
                C/C:\t{self.numero}
                Titular\t{self.cliente.nome}"""
    
class Historico:
    def __init__(self, transacoes):
        self._transacoes = []

        @property
        def transacoes(self):
            return self._transacoes
        
        def adicionar_transacao(self, transacao):
            self._transacoes.append({
                "tipo" : transacao.__class__.__name__,
                "valor" : transacao.valor,
                "data" : datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            })

class Transacao(ABC):
    pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso = conta.sacar(self.valor)

        if sucesso:
            conta.Historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso = conta.depositar(self.valor)

        if sucesso:
            conta.Historico.adicionar_transacao(self)

        