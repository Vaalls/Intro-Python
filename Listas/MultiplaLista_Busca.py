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
    resposta = input("Digite \"S\" para continuar").upper()

busca = input("\n Digite o nome do equipamento que deseja buscar: ")
for indice in range(0,len(equipamentos)):
    if busca == equipamentos[indice]:
        print("Valor....", valores[indice])
        print("Numero de série....", seriais[indice])
        print("Departamento...", departamento[indice])
