''' 
DICIONARIOS:
ARMAZENAMENTO DE INFORMAÇÕES MAIS COMPLEXAS DO QUE TUPLAS E LISTAS

> principalmente usado para armazenamento de usuarios

dicionarios: {}
tuplas: ()
listas: []
'''
#desafio de cadastro de aluno com dicionarios

def aluno_cadastro():
    
    aluno = {
        'nome': input("Digite o nome do aluno= "),
    'idade': input("Digite a idade do aluno= "),
    'nota': input("Digite a nota do aluno= ")

    }

    print(f"O aluno {aluno['nome']}, que tem {aluno['idade']} de idade, tirou a seguinte nota\n {aluno['nota']}")


opt = 0

while opt !=3:
    print('1- adicionar alunos da lista= ')
    print('2- calcular quanto falta para a formação= ')
    print('3- finaliza o programa= ')

    aluno_cadastro()

    opt = int(input("Insira a opção escolhida: "))

    if opt == 1:
        aluno_cadastro()
    elif opt == 2:
        calc={aluno_cadastro['idade']} < 17
        if calc < 17:
            print('precisa de alguns anos para finalizar')
        else:
            print('vc nem deveria estar aqui, pra começo de conversa')
    elif opt == 3:
        print('programa finalizado')
    else:
        print('opção invalida. tente novamente')

        

''' 
usuario = {'nome': "Andre",
    'idade': 45}

#modificar o dicionario
usuario['idade'] = 25

#adicionando
usuario["cidade"] = "Sâo Paulo"
#print(usuario['nome'])

#print(usuario['idade'])

print(usuario)
'''

