'''
FOR -> quando é estimado a quantidade de vezes que precisa
repetir uma tarefa. exemplo mais concreto, quandotem range

WHILE -> quando não é estimado a quantidade de vezes que
precisa repetir uma tarefa. vai depender de uma condição
'''

'''
for i in range(0, 50, 10):
    print(i)

i = 0
while i <= 10:
    print(i)
    i = i + 2
'''
senha = ''

while senha != '123':
    senha = input("Diga sua senha: ")

print("acesso liberado")
