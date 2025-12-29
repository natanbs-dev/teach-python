''' 
DICIONARIOS:
ARMAZENAMENTO DE INFORMAÇÕES MAIS COMPLEXAS DO QUE TUPLAS E LISTAS

> principalmente usado para armazenamento de usuarios

dicionarios: {}
tuplas: ()
listas: []
'''
#desafio de cadastro de aluno com dicionarios

aluno = {
    'nome': input("Digite o nome do aluno= "),
'idade': input("Digite a idade do aluno= "),
'nota': input("Digite a nota do aluno= ")

}

print(f"O aluno {aluno['nome']}, que tem {aluno['idade']} de idade, tirou a seguinte nota\n {aluno['nota']}")



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

