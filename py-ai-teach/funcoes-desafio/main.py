from funcoes import saudacao, somar, verificar_maioridade
#from test_m import operacao


#saudacao('caucaso')

#operacao()

#verificar_maioridade()

idade = int(input("digite a sua idade: "))

if verificar_maioridade(idade):
    print('você é maior de idade')

else:
    print('você é menor de idade')
