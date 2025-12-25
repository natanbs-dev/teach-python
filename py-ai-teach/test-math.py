def soma():
    n1= float(input("n1: "))
    n2 = float(input("n2:"))
    soma1 = n1+n2
    print(f"result é {soma1}")

def percentual_desconto():
    n1 = int(input("\nporcentagem: "))
    n2 = int(input("total : "))

    porc = (n1 * n2) / 100

    porc_total = n2 - porc

    print("====" * 50)

    print(f"Valor da Porcentagem: {n1}%"
          f"\nValor total: R${n2}"
          f"\nlogo, o valor da porcentagem é {porc}"
          f"\nSendo assim, valor com o desconto é de R${porc_total}")

    print("====" * 50)
def operacao():
    opt = 0

    while opt !=9:
        print("(1) SOMA" )
        print("(2) PORCENTAGEM")
        print("(9) para sair")
        print("===" * 30)
        opt = int(input("\ndigite o número escolhido== "))

        if opt == 1:
            soma()
        elif opt ==2:
            percentual_desconto()
        elif opt == 9:
            print ("===" * 30)
            print("programa finalizado")
        else:
            print("escolha invalida")

operacao()