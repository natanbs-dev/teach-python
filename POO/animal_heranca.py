# heranca multipla e heranca de diversos niveis

##grand father' class
class Animal:
    def __init__(self,nome):
        self.nome = nome

# father' class
class Predador(Animal):
    def caca(self):
        print(f'este animal {self.nome} está caçando')

# father' class
class Presa(Animal):
    def fugindo(self):
        print(f'Sendo o {self.nome}!! fugindo do caçador.')

class Coelho(Presa):
    pass

class Tigre(Predador):
    pass

class Golfinho(Presa, Predador):
    pass


coelho1 = Coelho('bunny')
coelho1.fugindo()

golfinho1 = Golfinho('billy willie')
golfinho1.caca()
golfinho1.fugindo()