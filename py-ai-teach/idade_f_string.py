def calc_idade_five():
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    calc = idade + 5
    print(f'Olá, {nome}!! Sua idade atual é {idade}!! \n\n Mas essa será sua idade daqui'
          f' a 5 anos === {calc} == ')

calc_idade_five()