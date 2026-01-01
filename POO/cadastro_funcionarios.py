class Funcionario:
    def __init__(self, nome, idade, cargo):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo
 
    def informacoes(self):
        print('***' * 20)
        print(f'NOME={self.nome} \nIDADE={self.idade} \nCARGO={self.cargo}')
        print('***' * 20)

    def promover(self, novo_cargo):
        print('*' * 20)
        print(f'o novo cargo de {self.nome} é {novo_cargo}. Sendo que o cargo anterior era {self.cargo}')
        print('*' * 20)

    def atualizar_idade(self, nova_idade):
        if nova_idade > self.idade:
            print(f'Atualizando a idade de {self.idade} para {nova_idade}')
        else:
            print(f'a nova idade precisa ser maior que a antiga')
        print('**' * 20)


funcionario1 = Funcionario('natan', 25, 'programador junior')
funcionario2 = Funcionario('gabriel', 46, 'assistente estagiario')

funcionario1.atualizar_idade(56)
funcionario1.promover('programador pleno')
funcionario2.promover('assistente pleno')

#funcionario1.informacoes()