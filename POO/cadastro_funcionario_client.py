class Pessoa: 
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print('***' *20)
        print(f'NOME={self.nome} \nIDADE={self.idade}')

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade) #vai puxar as informações da classe pai, PESSOA.
        self.cargo = cargo

    def trabalhar(self):
        print(f'{self.nome} está trabalhando como {self.cargo}')

class Cliente(Pessoa):
    def __init__(self, nome, idade, saldo):
        super().__init__(nome, idade) #vai puxar as informações da classe pai, PESSOA.
        self.saldo = saldo

    def comprar(self, valor_compra):
        if valor_compra <= self.saldo:
            self.saldo -= valor_compra
            print(f' A sua compra de {valor_compra} foi aprovada. \nSeu saldo atual é de {self.saldo}')
        else:
            print(f'saldo insuficiente, {self.nome}')

    
# f1 = Funcionario('jonas carlos', '56', 'programador')
# f1.apresentar()
# f1.trabalhar()

c1 = Cliente('arthur', 65, 200)
c1.apresentar()
c1.comprar(300)