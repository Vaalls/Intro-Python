#inventario
inventario = []
resposta = "S"
while(resposta == "S"):
    inventario.append(input("Equipamento: "))
    inventario.append(float(input("Valor: ")))
    inventario.append(int(input("Numero de série: ")))
    inventario.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper() #feito para inserir a aspas no print


for elemento in inventario:
    print(elemento)

