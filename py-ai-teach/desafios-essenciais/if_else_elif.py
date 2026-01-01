def nota_faculdade():
    opt = 0

    while opt != 1:
        nota_aluno = float(input("nota aluno: "))

        if nota_aluno <= 5:
            print("você estará de recuperação")
        elif nota_aluno >= 6 and nota_aluno <= 7:
            print("você terá que fazer uma segunda prova")
        elif nota_aluno >= 8 and nota_aluno <= 10:
            print("você já passou e entrará de férias amanhã!!!!!")
        else:
            print("digitou algo errado")
#nota_faculdade()

def autorizacao():
    idade = int(input("idade: "))
    autorizacao_pais = str(input("tem autorização dos pais?" + "(s/n)"))

    if idade >= 18:
        print("Acesso ao sistema liberado")
    elif idade >= 16 and autorizacao_pais == "s":
        print("Acesso so sistema liberado via autorização")
    else:
        print("acesso negado")

autorizacao()