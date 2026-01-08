"""
== igual
!= diferente
>= maior
<= menor
and
or
not
"""
from enum import nonmember
from operator import truediv
"""
n1= 10
n2 =20

print(n1 == n2) #igual a
print(n1 != n2) #diferente de
"""
def dirigir():
    idade = int(input("IDADE="))
    carteira = True
    verificador = idade >=18 and carteira
    #print(verificador)

    if verificador == True:
        print("você está nos conformes das leis")
    elif not verificador == False:
        print("vish... se a policia te pegar andando de carro sem carteira.....")

dirigir()

def verificar_login():
    user = str(input("username: "))
    password = str(input("password: "))
    login_valido = user == "admin" and password == "admin"

    print(f"login valido = {login_valido}")

#verificar_login()
