equipamentos = []
valores = []
seriais = []
departamento = []
resposta = "S"

while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Numero de série: ")))
    departamento.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar")

for indice in range(0,len(equipamentos)):
    print("\nEquipamento...", (indice+1))
    print("Nome...", equipamentos[indice])
    print("Valor...", valores[indice])
    print("Numero de série...", seriais[indice])
    print("Departamento...", departamento[indice])