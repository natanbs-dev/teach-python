class Carro:
    def __init__(self, ano, cor):
        self.cor = cor
        self.ano = ano 
        self.on = True


    def mostrar_informacoes(self,):
        print(f'\ncor= {self.cor}\nano= {self.ano}')
        
    def mostar_ligado(self):
        if not self.on:
            self.ligado = True
            print(f"o carro, do ano {self.ano} , foi ligado")
        else:
            print("o carro já estava desligado")

    def mostrar_desligado(self):
        if self.on:
            self.on = False
            print("o carro foi desligado")
        else:
            print('o carro estava desligado')
    
carro1 = Carro(2025, 'vermelho')

carro1.mostrar_informacoes()
carro1.mostar_ligado()
