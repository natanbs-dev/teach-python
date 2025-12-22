def porcentagem():
      n1 = int(input("\nporcentagem: "))
      n2 = int(input("total : "))

      porc = (n1 * n2) / 100

      porc_total = n2 - porc

      print ("====" *50 )

      print(f"Valor da Porcentagem: {n1}%"
            f"\nValor total: R${n2}"
            f"\nlogo, o valor da porcentagem é {porc}"
            f"\nO valor com o desconto é de R${porc_total}")


porcentagem()


if False:
      print(f'Olá, {nome}!! Sua idade atual é {idade}!! \n\n Mas essa será sua idade daqui'
            f' a 5 anos === {calc} == ')
