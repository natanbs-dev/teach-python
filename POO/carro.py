class Carro:
    def __init__(self, ano, cor):
        self.cor = cor
        self.ano = ano 
        self.ligado = True
        self.seta = None


    def informacoes(self,):
        print(f'\ncor= {self.cor}\nano= {self.ano}')
        
    def mostar_ligado(self):
        if not self.ligado:
            self.ligado = True
            print(f"o carro, do ano {self.ano} , foi ligado")
        else:
            print("o carro já estava desligado")

    def mostrar_desligado(self):
        if self.ligado:
            self.ligado = False
            print("o carro foi desligado")
        else:
            print('o carro estava desligado')

    def ligar_seta(self, direcao):
        if not self.ligado:
            print('ligue o carro :)')
            return
        
        self.seta = direcao
        print(f'Seta ligada para a {self.seta}')
    
carro1 = Carro(2025, 'vermelho')

carro1.informacoes()
carro1.mostar_ligado()
carro1.ligar_seta('right')