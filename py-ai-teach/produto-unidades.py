"""
calcular quantos dias um produto duraria se a pessoa usar X unidades por dia
"""
def produto_unidades():
    valor_unidades = int(input("UNIDADES-TOTAIS="))
    consumo_dia = int(input("CONSUMO_DIA="))
    calc = valor_unidades / consumo_dia
    print("--" * 30)
    print(f'O produto irá durar {int(calc)} dias se você continuar a consumir {consumo_dia} por dia')
    print("--" * 30)

produto_unidades()