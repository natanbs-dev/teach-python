def saudacoes(nome, idade):
    print(f"olá {nome} idade sendo {idade}" )

#saudacoes('carlos', 26)
 
def somar(n1, n2):
    soma= n1 + n2
    print(soma)

#somar(5,6)

def calcular_desconto(preco, porcentagem):
    return preco - (preco * porcentagem / 100)

valor_final = calcular_desconto(1010, 25)
print(f'o valor final com desconto é R${valor_final:.2f}')